#!/bin/bash
docker run --device /dev/i2c-1 -p 31337:31337/udp -it test_replay
