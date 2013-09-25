#!/bin/sh
#Requirement: sudo apt-get install kexec-tools

sudo kexec -l /boot/vmlinuz-`uname -r` --initrd=/boot/initrd.img-`uname -r` --append="`cat /proc/cmdline`"

sudo kexec -e

