#!/bin/bash

caddy&
CADDY_PID=$!
echo "caddy is running as $CADDY_PID"

echo "Debug at http://localhost:9222"
/opt/google/chrome/chrome --kiosk --remote-debugging-port=9222 http://localhost:2020/sign.html

echo "Killing caddy"
kill $CADDY_PID
