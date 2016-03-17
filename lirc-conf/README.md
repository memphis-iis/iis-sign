# IIS-Sign LIRC conf extras

This directory is an attempt to help you jump start projector control with
LIRC. Note that recent versions of Ubuntu have an older lirc. As a result,
the combination of lircd and our USB-UIRT device tends to segfault. You can
fix this by custom building your own lirc. Note that the rest of this document
assumes that this is what you did.

## Building lirc

First you should also read: http://www.lirc.org/html/install.html. You'll need
all the required dependencies. You should also install the ftdi/usb optional
dependencies:

````
$ sudo apt-get libusb-dev libftdi-dev libftdi1-dev
````

You should also remove any previous packaged version of lirc:

````
$ sudo apt-get purge lirc lirc-x
````

After that it's as simple as cloning the repository, configuring, building,
and installing:

````
$ git clone git://git.code.sf.net/p/lirc/git lirc-git
$ cd lirc-git
$ ./autogen.sh
$ ./configure --prefix=/usr --sysconfdir=/etc
$ make
$ sudo make install
````

Note that after the `configure` step you should verify that you still have the
ftdi and usb build options enabled.

You can now proceed to configure your installation.

## Configuring the installed lirc

You DO need to provide a remote configuration file:

* If you are using the Casio wall-mounted XJ-UT310WN ultra short throw
  projector, you can use the file `casio.conf` from the directory
* If you are using the ViewSonic ultra portable projector, you can use the file
  `viewsonic.conf` from this directory

Regardless, you should copy the appropriate file to `/etc/lirc/lircd.conf.d/`

## Running lircd

You'll need to make sure `lircd` is not running when you use `irrecord`.
Otherwise, you'll need to run `lircd`. For other operations (e.g. debugging
input with `irw` or sending signals with `irsend`) you need to be running
`lircd`. If you build/configured lirc as above, you can run lirc with our
USB UIRT device like so:

````
$ sudo lircd --nodaemon -d /dev/ttyUSB0 --driver=usb_uirt_raw
````

With this running you could watch IR signals received:

````
$ irw /var/run/lirc/lircd
````

or you could send a signal:

````
$ irsend -d /var/run/lirc/lircd SEND_ONCE ViewSonic-PLED-W500-UltraPortableProjector key_power
````

## Putting it all together

With all that under your belt, you're ready for one-off IR signal
transmission. To make this easier, we provide the simple script `send_power.sh`
in this directory. You should run it as root (or via sudo):

````
$ ./send_power.sh
````

It starts lircd, sends a key_power signal, and then shuts down lircd. All that
you need to do is copy it somewhere, change the configuration section to match
(i.e. choose the correct remote control name), and schedule it to run as the
root user (e.g. via `sudo crontab -e`).

## Notes on casio.conf

Some keys were not recorded since there weren't any good matches in the lirc
remote key namespace. The skipped keys are:

* Keystone +/- buttons
* Blank, Freeze, and Echo buttons (the row directly beneath the Keystone,
  D-Zoom, and Volume button pairs)
* Timer, Auto, Aspect, and Func buttons (the column of small buttons on the
  lower right side of the remote)

## Notes on viewsonic.conf

Sample configuration for the ViewSonic projector we originally bought for our
project (we are now using a different projector). Made originally with the
Ubuntu-packaged irrecord command: `sudo irrecord --driver=usb_uirt_raw
ViewSonic-PLED-W500-UltraPortableProjector.conf` (with lircd NOT running)


Some nonstandard keys we chose:

* KEY_TV for the "HDMI" button
* KEY_VCR for the "SD/USB" button
* KEY_CONFIG for the "My Button" button
* KEY_SYSRQ for "Auto Sync" button
* KEY_SWITCHVIDEOMODE for "Color Mode" button
* KEY_SELECT for "Source" button

## irrecord button names

When using irrecord, you'll need to use the predefined key names. See the file
`lirc-key-list.txt` in this directory.
