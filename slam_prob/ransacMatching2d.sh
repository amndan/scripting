#/bin/sh

rm -r /tmp/trace2/
cd $OBVIOUSLY_ROOT/build/release
MAKE_RES=$(make)
#echo $MAKE_RES
if [ "$MAKE_RES"="0" ] 
then
	echo "Make completed"
else
	echo "Make fail"
	exit 1
fi

$OBVIOUSLY_ROOT/build/release/applications/ransac_matching2D_2
cd /tmp/trace2
gnuplot trace.gpi
eog *.png

exit 0

