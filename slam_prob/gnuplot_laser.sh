#!/bin/sh

search_dir="/tmp/trace"

echo $search_dir

mkdir $search_dir/images

for entry in $search_dir/*
do
	cd $entry
	gnuplot trace.gpi
	# all traces to one image (4 columns)
	montage -mode concatenate -tile 3x ./trace*.png ${entry##*/}.jpg
	#copy generated image to image folder
	cp ${entry##*/}.jpg $search_dir/images
	echo $entry
done

exit 0
