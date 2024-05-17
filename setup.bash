#! /usr/bin/bash

echo "Downloading necessary packages..."
# OS packages
sudo apt-get install openssl
echo ""
# python packages
sudo apt-get install python3-flask
sudo apt-get install python3-pillow

cd ..
curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/main/rgb-matrix.sh >rgb-matrix.sh
sudo bash rgb-matrix.sh

cd imgRecord

# self-signed certificate
openssl req -newkey rsa:4096 -x509 -sha512 -days 365 -nodes -out cert.pem -keyout key.pem
