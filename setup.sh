#!/bin/bash
echo "Installing Cael Core..."
mkdir -p ~/Cael/Journal ~/Cael/Health ~/Cael/Calendar ~/Cael/Tasks
mkdir -p ~/.local/share/applications
cp cael-core.desktop ~/.local/share/applications/
echo "Cael Core installation complete."
