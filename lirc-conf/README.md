# IIS Sign LIRC conf extras

This directory is an attempt to help you jump start projector control with
LIRC. Contents:

## hardware.conf

An attempt to keep a reasonably up-to-date copy of the config file you should
use for LIRC (at `/etc/lirc`)

## ViewSonic-PLED-W500-UltraPortableProjector.conf

Sample configuration for the ViewSonic projector we originally bought for our
project (we are now using a different projector). Made with
`sudo irrecord --driver=usb_uirt_raw ViewSonic-PLED-W500-UltraPortableProjector.conf`
