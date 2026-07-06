#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE[0]}")/../../caching.sh"

# Singleton lock: chỉ 1 instance bt_wait.sh được chạy cùng lúc
# LOCK="$QS_RUN_DIR/qs_bt_wait.lock"
# exec 9>"$LOCK"
# flock -n 9 || { sleep infinity; exit 0; }

PIPE="$QS_RUN_DIR/qs_bt_wait_$$.fifo"
mkfifo "$PIPE" 2>/dev/null

PID1="" PID2=""

cleanup() {
    rm -f "$PIPE"
    for pid in "$PID1" "$PID2"; do
        [ -n "$pid" ] || continue
        kill -TERM "-$pid" 2>/dev/null
        kill -TERM "$pid" 2>/dev/null
    done
    # exit removed
}
trap 'cleanup' EXIT; trap 'cleanup; exit 143' TERM INT

# Chạy mỗi dbus-monitor trong session riêng để kill chính xác bằng PGID
LC_ALL=C setsid dbus-monitor --system "type='signal',interface='org.freedesktop.DBus.Properties',member='PropertiesChanged',arg0='org.bluez.Device1'" 2>/dev/null | grep --line-buffered 'string "Connected"' > "$PIPE" &
PID1=$!
LC_ALL=C setsid dbus-monitor --system "type='signal',interface='org.freedesktop.DBus.Properties',member='PropertiesChanged',arg0='org.bluez.Adapter1'" 2>/dev/null | grep --line-buffered 'string "Powered"' > "$PIPE" &
PID2=$!

read -r _ < "$PIPE"
