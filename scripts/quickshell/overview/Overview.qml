import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import Quickshell
import Quickshell.Io
import Quickshell.Wayland
import "../"

Variants {
    id: overviewVariants
    model: Quickshell.screens

    property var workspacesData: []
    property var windowsData: []

    delegate: Component {
        PanelWindow {
            id: root
            required property var modelData
            screen: modelData

            visible: Config.overviewOpen

            WlrLayershell.namespace: "quickshell:overview-blur"
            WlrLayershell.layer: WlrLayer.Overlay
            WlrLayershell.keyboardFocus: Config.overviewOpen ? WlrKeyboardFocus.Exclusive : WlrKeyboardFocus.None
            color: "transparent"

            anchors {
                top: true
                bottom: true
                left: true
                right: true
            }

            ToplevelManager {
                id: toplevelManager
            }

            Process {
                id: niriWorkspacesProcess
                command: ["niri", "msg", "-j", "workspaces"]
                stdout: StdioCollector {
                    onStreamFinished: {
                        try {
                            overviewVariants.workspacesData = JSON.parse(this.text.trim())
                        } catch(e) {}
                    }
                }
            }

            Process {
                id: niriWindowsProcess
                command: ["niri", "msg", "-j", "windows"]
                stdout: StdioCollector {
                    onStreamFinished: {
                        try {
                            overviewVariants.windowsData = JSON.parse(this.text.trim())
                        } catch(e) {}
                    }
                }
            }

            IpcHandler {
                target: "overview"
                function toggle() {
                    Config.overviewOpen = !Config.overviewOpen
                }
                function open() {
                    Config.overviewOpen = true
                }
                function close() {
                    Config.overviewOpen = false
                }
            }

            MatugenColors { id: mocha }

            onVisibleChanged: {
                Config.sh("echo " + (visible ? "1" : "0") + " > /tmp/overview_open")
                if (visible) {
                    console.log("[Overview] Opened — refreshing data")
                    niriWorkspacesProcess.running = true
                    niriWindowsProcess.running = true
                }
            }

            Rectangle {
                anchors.fill: parent
                color: Qt.rgba(mocha.base.r, mocha.base.g, mocha.base.b, 0.4)

                MouseArea {
                    anchors.fill: parent
                    onClicked: Config.overviewOpen = false
                }
            }

            Item {
                id: container
                anchors.fill: parent
                focus: Config.overviewOpen

                opacity: Config.overviewOpen ? 1.0 : 0.0
                Behavior on opacity {
                    NumberAnimation {
                        duration: 180
                        easing.type: Easing.OutCubic
                    }
                }

                Keys.onPressed: (event) => {
                    if (event.key === Qt.Key_Escape || event.key === Qt.Key_Tab) {
                        Config.overviewOpen = false
                        event.accepted = true
                    } else if (event.key >= Qt.Key_1 && event.key <= Qt.Key_8) {
                        let ws = event.key - Qt.Key_0
                        Config.overviewOpen = false
                        Config.sh("niri msg action focus-workspace " + ws)
                        event.accepted = true
                    }
                }

                Column {
                    anchors.fill: parent
                    anchors.margins: 40
                    spacing: 20

                    Text {
                        anchors.horizontalCenter: parent.horizontalCenter
                        text: "Workspaces Overview"
                        font.family: "Outfit"
                        font.pixelSize: 28
                        font.weight: Font.Bold
                        color: mocha.text
                    }

                    // Horizontal list of workspaces
                    ListView {
                        id: workspacesListView
                        width: parent.width
                        height: parent.height - 80
                        orientation: ListView.Horizontal
                        spacing: 24
                        model: overviewVariants.workspacesData

                        delegate: Rectangle {
                            id: wsBox
                            required property var modelData
                            property int workspaceId: modelData.id
                            property bool isFocused: modelData.is_active || modelData.active

                            width: root.screen.width * 0.38
                            height: parent.height - 20
                            radius: 16

                            color: isFocused
                                   ? Qt.rgba(mocha.surface0.r, mocha.surface0.g, mocha.surface0.b, 0.75)
                                   : Qt.rgba(mocha.surface0.r, mocha.surface0.g, mocha.surface0.b, 0.3)
                            border.width: isFocused ? 2 : 1
                            border.color: isFocused
                                          ? mocha.mauve
                                          : Qt.rgba(mocha.text.r, mocha.text.g, mocha.text.b, 0.1)

                            Behavior on color { ColorAnimation { duration: 150 } }
                            Behavior on border.color { ColorAnimation { duration: 150 } }

                            Text {
                                id: headerText
                                anchors.left: parent.left
                                anchors.top: parent.top
                                anchors.margins: 16
                                text: "Workspace " + wsBox.workspaceId
                                font.family: "Outfit"
                                font.pixelSize: 20
                                font.weight: Font.Bold
                                color: wsBox.isFocused ? mocha.mauve : mocha.subtext0
                                z: 10
                            }

                            // Horizontal scroll view of windows inside this workspace
                            ListView {
                                id: windowsListView
                                anchors.top: headerText.bottom
                                anchors.bottom: parent.bottom
                                anchors.left: parent.left
                                anchors.right: parent.right
                                anchors.margins: 16
                                orientation: ListView.Horizontal
                                spacing: 12
                                model: {
                                    let filtered = []
                                    let winData = overviewVariants.windowsData || []
                                    for (let i = 0; i < winData.length; i++) {
                                        if (winData[i].workspace_id === wsBox.workspaceId) {
                                            filtered.push(winData[i])
                                        }
                                    }
                                    return filtered
                                }

                                delegate: Item {
                                    required property var modelData
                                    width: wsBox.width * 0.44
                                    height: parent.height - 10

                                    OverviewWindow {
                                        anchors.fill: parent
                                        wsScale: 1.0
                                        screenX: 0
                                        screenY: 0
                                        title: modelData.title || "Window"
                                        appId: modelData.app_id || ""
                                        isFocused: modelData.is_focused || false
                                        toplevel: {
                                            let win = modelData
                                            let arr = toplevelManager.toplevels
                                            if (!arr) return null
                                            for (let j = 0; j < arr.count; j++) {
                                                let tl = arr.get(j)
                                                if (tl && tl.title === win.title && tl.appId === win.app_id) {
                                                    return tl
                                                }
                                            }
                                            return null
                                        }
                                    }
                                }
                            }

                            MouseArea {
                                anchors.fill: parent
                                z: -1
                                onClicked: {
                                    Config.overviewOpen = false
                                    Config.sh("niri msg action focus-workspace " + wsBox.workspaceId)
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
