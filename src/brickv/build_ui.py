#!/usr/bin/env python

import os

def system(command):
    if os.system(command) != 0:
        exit(1)

system("pyuic4 -o ui_mainwindow.py ui/brickv.ui")
system("pyuic4 -o ui_flashing.py ui/flashing.ui")
system("pyuic4 -o ui_advanced.py ui/advanced.ui")
