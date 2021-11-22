#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

/usr/bin/qemu-system-x86_64 \
    -s \
	-m 64M \
	-cpu kvm64,+smep,+smap \
	-kernel $SCRIPT_DIR/bzImage \
	-initrd $SCRIPT_DIR/initramfs.cpio.gz \
	-nographic \
	-monitor none \
	-append "console=ttyS0 nokaslr quiet panic=1" \
	-no-reboot
