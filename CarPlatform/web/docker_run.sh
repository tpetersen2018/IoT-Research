#!/bin/bash
docker run --device /dev/i2c-1 -p 8080:80 -it web
