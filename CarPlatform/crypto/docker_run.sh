#!/bin/bash
docker run --device /dev/i2c-1 -p 33047:33047/udp -it test_crypto
