#!/usr/bin/env bash

SHELL_PATH="$HOME/.config/niri/bin/quickshell/Shell.qml"

# 1. Reload Niri config (load-config-file không re-spawn các spawn-at-startup)
niri msg action load-config-file

# 2. Reload Quickshell bằng IPC (gọi Quickshell.reload bên trong QML)
quickshell -p "$SHELL_PATH" ipc call main forceReload >/dev/null 2>&1
sleep 0.3

# 3. Nếu IPC không được hoặc quickshell chết, hard restart
if ! pgrep -f "quickshell.*Shell.qml" >/dev/null; then
    quickshell -p "$SHELL_PATH" >/dev/null 2>&1 &
    disown
fi
