#!/bin/sh
#
# Perform spatio-temporal subsetting of input files

#vars_sfc="psl"
#vars_500="ua500 va500"
#vars_1000="zg1000"
#vars_cst="z lsm"

#inc="1d"
#period="19790101_20161231"
#model="ERAI"
#latbox="30.,60."
#lonbox="330.,30."
#timesub="0,3650"
filelist=$1
inc=$2
period=$3
model=$4
latbox=$5
lonbox=$6
time=$7

outfile="${period}_${model}.nc"

mkdir results

# ncks -d time,0,365 -d latitude,${latbox} -d longitude,-30.,30. uas_day_CNRM-CM5_rcp85_r1i1p1_20060101-21001231.nc out.nc
#-rwxr-xr-x 1 page globc 1.6G Sep 22 16:01 psl_1d_19790101_20161231_ERAI.nc*
#-rwxr-xr-x 1 page globc 1.6G Sep 22 16:02 ua500_1d_19790101_20161231_ERAI.nc*
#-rwxr-xr-x 1 page globc 1.6G Sep 22 16:02 va500_1d_19790101_20161231_ERAI.nc*
#-rw-r--r-- 1 page globc 1.6G Sep 25 14:21 zg1000_1d_19790101_20161231_ERAI.nc
#-rwxr-xr-x 1 page globc  60K Sep 22 15:59 z_ERAI.nc*

rm -f results/${outfile}

files=`awk '{print $2}' $filelist`

for i in ${files}
do

filename=$i
var=`echo $filename | awk 'BEGIN {FS="_"} {print $1}'`

rm -f results/$filename
if [ $var = "z" -o $var = "lsm" ]
then
  ncks -O -d latitude,${latbox} -d longitude,${lonbox} ${filename} results/${filename}
else
  ncks -O -d time,${time} -d latitude,${latbox} -d longitude,${lonbox} ${filename} results/${filename}
fi
if [ ! -s results/${outfile} ]
then
  cp results/${filename} results/${outfile}
else
  ncks -h -A results/${filename} results/${outfile}
fi

done
