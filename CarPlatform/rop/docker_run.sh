#!/bin/bash
docker run --device /dev/i2c-1 -p 1337:1337 -it rop
