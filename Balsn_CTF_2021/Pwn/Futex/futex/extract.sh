#!/bin/sh
 
sudo rm -r ./fs
mkdir fs
cd fs
cpio -idv < ../initramfs.cpio
cd ../
