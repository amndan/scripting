#!/bin/sh

OBVIOUSLY="/home/amndan/Software/obviously/build/release/"
ACTUAL=`pwd`
CATKIN="/home/amndan/dev/bobby_ws/"

cd $OBVIOUSLY
make
make install
cd $CATKIN
rm -r ./build/ohm_tsd_slam/
catkin_make --pkg ohm_tsd_slam

