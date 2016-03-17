#!/bin/bash

# Helper to send power button signal via an attached USB UIRT remote. This
# script assumes that you have build and configured LIRC per README.md in
# this directory.

# Checks for what we need
if [ "$(id -u)" != "0" ]; then
    echo "You must run this script as root (probably using sudo)"
    echo "YES - we should probably change this"
    exit 1
fi


# Configuration
LIRCD_DEV=/dev/ttyUSB0
DRIVER=usb_uirt_raw
REMOTE=casio-yt-140
IRSEND_DEV=/var/run/lirc/lircd

# start lircd
echo "Insuring /var/run/lirc"
mkdir -p /var/run/lirc
echo "Starting lircd..."
lircd --nodaemon -d $LIRCD_DEV --driver=$DRIVER &
LIRCD_PID=$!
sleep 1  # Hack to make sure everything OK
echo "...started lircd at PID $LIRCD_PID"

# Actual send
echo "Using irsend for key_power"
irsend -d $IRSEND_DEV SEND_ONCE $REMOTE key_power
sleep 1  # Hack to make sure everything OK

# stop lircd
echo "Stopping lircd PID $LIRCD_PID..."
kill $LIRCD_PID
