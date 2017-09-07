#!/bin/bash

caddy&
CADDY_PID=$!
echo "caddy is running as $CADDY_PID"

QS=""
if [ x"$1" != x ]; then
    QS="?$1"
    echo "Using querystring $QS"
fi

echo "Debug at http://localhost:9222"
/opt/google/chrome/chrome --kiosk --disable-session-crashed-bubble --remote-debugging-port=9222 "http://localhost:2020/sign.html$QS"

echo "Killing caddy"
kill $CADDY_PID
