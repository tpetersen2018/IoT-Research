# Overflow2

This module tests user's ability to smash the stack and overwrite the return address


## Building

Run `bash docker_build.sh` to make a container called **overflow2**

## Deploying

Run `bash docker_run.sh` to run the container as a service.
**PORT - 1337**

## Exploiting

- Return address is located after 24 bytes.
- Craft payload with 24 A's, followed by the address of driver_menu()
- Save to file. Then send in using `cat exploit - | nc <ip> <port>` 
