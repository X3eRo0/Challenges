#!/bin/bash

pushd fs > /dev/null
find . -print0 | cpio --null -ov --format=newc 2>/dev/null | gzip -9 > ../initramfs.cpio.gz
popd > /dev/null
