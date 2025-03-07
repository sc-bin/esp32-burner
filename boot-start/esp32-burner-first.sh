#!/bin/bash
file_path=${BASH_SOURCE[0]}

sudo systemctl enable lightdm.service
sudo set-lcd lcd35-st7796 install
sudo rm $shell_first
rm $file_path
sudo reboot