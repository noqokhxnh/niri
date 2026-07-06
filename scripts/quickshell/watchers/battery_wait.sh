#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE[0]}")/../../caching.sh"

# Singleton lock: chỉ 1 instance battery_wait.sh được chạy cùng lúc
# LOCK="$QS_RUN_DIR/qs_battery_wait.lock"
# exec 9>"$LOCK"
# flock -n 9 || { sleep infinity; exit 0; }

PIPE="$QS_RUN_DIR/qs_battery_wait_$$.fifo"
mkfifo "$PIPE" 2>/dev/null

MONITOR_PID=""

cleanup() {
    rm -f "$PIPE"
    if [ -n "$MONITOR_PID" ]; then
        kill -TERM "-$MONITOR_PID" 2>/dev/null
        kill -TERM "$MONITOR_PID" 2>/dev/null
    fi
    # exit removed
}
trap 'cleanup' EXIT; trap 'cleanup; exit 143' TERM INT

# Chạy udevadm trong session riêng để kill chính xác bằng PGID
LC_ALL=C setsid udevadm monitor --subsystem-match=power_supply 2>/dev/null > "$PIPE" &
MONITOR_PID=$!

# Blocks until udevadm catches a change, OR 10 seconds pass (failsafe).
timeout 10 grep -m 1 "change" < "$PIPE" > /dev/null || true

