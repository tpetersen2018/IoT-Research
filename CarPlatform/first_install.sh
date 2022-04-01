# First download Docker
curl -sSL https://get.docker.com | sh
sudo usermod -aG docker ${USER}

# Now install pwntools
pip3 install unicorn
pip3 install pwntools

# reboot system
sudo reboot
