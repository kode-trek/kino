#!/bin/sh
sudo mount /dev/"$1" -t ntfs-3g -o permissions /media/"$2"
