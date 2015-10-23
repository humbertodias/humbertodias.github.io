#!/usr/bin/env bash

# Set start time so we know how long the bootstrap takes
T="$(date +%s)"

# Dependences
sudo apt-get --assume-yes update
sudo apt-get --assume-yes install xvfb python-pygame unzip

echo 'Downloading and copying the Game to /vagrant'
cd /vagrant
# wget "https://raw.githubusercontent.com/humbertodias/humbertodias.github.io/master/vagrant/pygame/asteroids_sprites.zip"
unzip asteroids_sprites.zip

# cd asteroids_sprites
# python asteroids.py

# Set start time so we know how long the bootstrap takes
T="$(date +%s)"