#!/bin/bash


# minctookit2
sudo apt-get install libc6 libstdc++6 imagemagick perl gdebi-core &&
sudo apt-get install libgl1-mesa-glx libglu1-mesa &&
echo you have to downlad package 1.9.17 Ubuntu 18.04 at https://bic-mni.github.io/
gdebi minc-toolkit-1.9.17-20190313-Ubuntu_18.04-x86_64.deb &&
echo "export PATH=/opt/minc/1.9.17/bin:$PATH" >> ~/.bashrc &&
source ~/.bashrc &&
echo "export LD_LIBRARY_PATH=/opt/minc/1.9.17/lib:$LD_LIBRARY_PATH" >> ~/.bashrc &&
source ~/.bashrc

# pyminc
git clone https://github.com/Mouse-Imaging-Centre/pyminc.git
cd pyminc || exit
python setup.py install

# minc-stuff
git clone https://github.com/Mouse-Imaging-Centre/minc-stuffs.git
cd minc-stuffs
git submodule update --init --recursive
./autogen.sh
./configure --with-build-path=/opt/minc/1.9.17/
make
sudo make install