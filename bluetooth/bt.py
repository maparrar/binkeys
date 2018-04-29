#!/usr/bin/python
from usb.core import find as finddev
dev = finddev(idVendor=0x13d3, idProduct=0x3362)
dev.reset()
