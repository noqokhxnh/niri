import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import Quickshell
import Quickshell.Io
import Quickshell.Wayland
import Quickshell.Hyprland
import "../"

Variants {
    id: overviewVariants
    model: Quickshell.screens

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

            HyprlandFocusGrab {
                id: grab
                windows: [root]
                active: Config.overviewOpen
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
                    Hyprland.refreshToplevels()
                    Hyprland.refreshWorkspaces()
                    refreshTimer.start()
                }
            }

            // Delayed refresh to ensure data arrives
            Timer {
                id: refreshTimer
                interval: 200
                repeat: false
                onTriggered: {
                    Hyprland.refreshToplevels()
                    Hyprland.refreshWorkspaces()
                    let tlCount = Hyprland.toplevels.values ? Hyprland.toplevels.values.length : 0
                    let wsCount = Hyprland.workspaces.values ? Hyprland.workspaces.values.length : 0
                    console.log("[Overview] Refreshed: " + tlCount + " toplevels, " + wsCount + " workspaces, focused=" + (Hyprland.focusedWorkspace ? Hyprland.focusedWorkspace.id : "none"))
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

            Connections {
                target: Hyprland
                function onRawEvent(event) {
                    let name = event.name || ""
                    if (Config.overviewOpen && (name === "openwindow" || name === "closewindow" || name === "movewindow" || name === "workspace")) {
                        Hyprland.refreshToplevels()
                        Hyprland.refreshWorkspaces()
                    }
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
                        Config.sh("hyprctl dispatch 'hl.dsp.focus({ workspace = " + ws + " })'")
                        event.accepted = true
                    }
                }

                Column {
                    anchors.centerIn: parent
                    spacing: 30

                    Text {
                        anchors.horizontalCenter: parent.horizontalCenter
                        text: "Workspaces"
                        font.family: "Outfit"
                        font.pixelSize: 28
                        font.weight: Font.Bold
                        color: mocha.text
                    }

                    Grid {
                        id: workspaceGrid
                        anchors.horizontalCenter: parent.horizontalCenter
                        columns: Math.ceil(Config.workspaceCount / 2)
                        rows: 2
                        spacing: 20

                        property real wsScale: 0.16
                        property real wsWidth: root.screen.width * wsScale
                        property real wsHeight: root.screen.height * wsScale

                        Repeater {
                            model: Config.workspaceCount
                            delegate: Rectangle {
                                id: wsBox
                                property int workspaceId: index + 1

                                // Find the matching HyprlandWorkspace object using .values array
                                property var hyprWs: {
                                    let wsModel = Hyprland.workspaces
                                    if (!wsModel) return null
                                    // Try .values first (array access)
                                    let arr = wsModel.values || []
                                    for (let i = 0; i < arr.length; i++) {
                                        if (arr[i] && arr[i].id === workspaceId) return arr[i]
                                    }
                                    // Fallback: try .count and .get()
                                    if (typeof wsModel.count === 'number') {
                                        for (let i = 0; i < wsModel.count; i++) {
                                            let ws = wsModel.get(i)
                                            if (ws && ws.id === workspaceId) return ws
                                        }
                                    }
                                    return null
                                }

                                property bool isFocused: Hyprland.focusedWorkspace ? (Hyprland.focusedWorkspace.id === workspaceId) : false

                                width: workspaceGrid.wsWidth
                                height: workspaceGrid.wsHeight
                                radius: 14

                                color: isFocused
                                       ? Qt.rgba(mocha.surface0.r, mocha.surface0.g, mocha.surface0.b, 0.7)
                                       : Qt.rgba(mocha.surface0.r, mocha.surface0.g, mocha.surface0.b, 0.3)
                                border.width: isFocused ? 2 : 1
                                border.color: isFocused
                                              ? mocha.mauve
                                              : Qt.rgba(mocha.text.r, mocha.text.g, mocha.text.b, 0.1)

                                Behavior on color { ColorAnimation { duration: 150 } }
                                Behavior on border.color { ColorAnimation { duration: 150 } }

                                Text {
                                    anchors.left: parent.left
                                    anchors.top: parent.top
                                    anchors.margins: 12
                                    text: wsBox.workspaceId
                                    font.family: "Outfit"
                                    font.pixelSize: 18
                                    font.weight: Font.Bold
                                    color: wsBox.isFocused ? mocha.mauve : mocha.subtext0
                                    z: 10
                                }

                                // Use workspace-level toplevels via .values
                                Repeater {
                                    model: {
                                        if (wsBox.hyprWs && wsBox.hyprWs.toplevels) {
                                            return wsBox.hyprWs.toplevels.values || []
                                        }
                                        return []
                                    }
                                    delegate: OverviewWindow {
                                        required property var modelData
                                        toplevel: modelData
                                        wsScale: workspaceGrid.wsScale
                                        screenX: root.screen.x
                                        screenY: root.screen.y
                                    }
                                }

                                MouseArea {
                                    anchors.fill: parent
                                    onClicked: {
                                        Config.overviewOpen = false
                                        Config.sh("hyprctl dispatch 'hl.dsp.focus({ workspace = " + wsBox.workspaceId + " })'")
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
