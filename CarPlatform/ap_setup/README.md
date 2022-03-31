# Setup Pi as Access Point

## Installation Instructions
 - Run the command `curl -ssL https://install.raspap.com | bash`
 - Let RaspAP install needed dependencies. You can choose to not install VPN features
 - Reboot Pi


## How to Configure
 - Go to browser and enter your IP. This will bring up RaspAP Config website
 - Sign in with default credentials `admin:secret`
 - Click on Hotspot and change settings like
    - SSID
    - Channel
    - PSK
 - Click on DHCP Server and change IP addresses to a unique hotspot.
 - Some things to change are:
    - Adapter IP Address Settings: IP Address, Default Gateway
    - DHCP Options: Starting IP Address, Ending IP Address
 - Click on Authentication and change default password. **Make sure you remember it!**
 - Reboot Pi

## Switching to Client Wifi
 - Turn off Access Point with the command `sudo systemctl stop hostapd`
 - Use Panda Wifi Adapter to connect to outside wifi


## Restarting Access Point
 - Enter command `sudo systemctl start hostapd`
