#! /bin/sh
set -x

path=/home/pi/reverse-grinder/fortolkningsdissonans/coronavirus_prediction
cd $path
python $path/main.py > $path/corona_pred.txt
