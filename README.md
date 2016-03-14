# IIS Signage Work

This is mainly about sign.html and it's supporting media files. This file
cycles among  pages so that we can have a changing dynamic display on our
ultra-short-projector.

We assume that we'll be running with Caddy.

Note that on the final computer driving the sign, you can use our test script,
but you'll probably want to add some site-specific changes. For example:

* Using `unclutter` to hide the mouse cursor
* Pulling the latest code from github.com before starting

## Extras includes

The lirc-conf directory includes helper configurations and a README for working
with LIRC and IR blasters
