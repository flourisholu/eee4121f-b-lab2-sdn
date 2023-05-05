#!/bin/bash

# Note: Mininet must be run as root.  So invoke this shell script
# using sudo.

~pox/pox.py forwarding.l2_learning misc.firewall &

gnome-terminal -- python sdn.py
