#/bib/bash
# -*- ENCODING: UTF-8 -*-
clear
echo '1. INSTALANDO PYTHON'
echo ' '
sudo apt-get install python3
echo ' '
echo '2. INSTALANDO OPENCV2'
echo ' '
sudo apt-get install libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqtgui4 libqt4-test
sudo pip3 install opencv-contrib-python==4.1.0.25
echo ' '
echo '3. INSTALANDO RPI-WS281X'
echo ' '
sudo pip3 install rpi-ws281x