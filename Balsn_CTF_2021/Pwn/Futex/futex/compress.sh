#!/bin/sh
 
rm ./initramfs.cpio
cd ./fs
find ./ -print0 | cpio --owner root --null -o --format=newc > ../initramfs.cpio
cd ../
