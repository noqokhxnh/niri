#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE[0]}")/../../caching.sh"

# Singleton lock: chỉ 1 instance audio_wait.sh được chạy cùng lúc
# LOCK="$QS_RUN_DIR/qs_audio_wait.lock"
# exec 9>"$LOCK"
# flock -n 9 || { sleep infinity; exit 0; }

PIPE="$QS_RUN_DIR/qs_audio_wait_$$.fifo"
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

# Chạy pactl trong session riêng để kill chính xác bằng PGID
LC_ALL=C setsid pactl subscribe 2>/dev/null > "$PIPE" &
MONITOR_PID=$!

grep -m 1 -E "sink|server" < "$PIPE" > /dev/null
