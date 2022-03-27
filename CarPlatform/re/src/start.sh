#!/bin/bash
python3 udpserver.py &
nc.traditional -lvp 1337 -e car

