#!/bin/sh
#
WORKDIR="$1"

#Working directory
if [ -z $WORKDIR ]
then
  WORKDIR="."
fi

cd $WORKDIR

# Executables
GETFILES=get_files.sh
EXTRACTDATA=extract_data.sh
TRACKS=make_tracks.abs
XMLASCII=tracking_xml2ascii.py
CREATEMAPS=create_track_maps

# Basemap directory
BASEMAPDIR=$HOME/tracking/data

# Create data directory
#
mkdir data

#### CONFIG
####
vars_sfc="psl"
vars_500="ua500 va500"
vars_1000="zg1000"
var_cst_z="z"
var_cst_lsm="lsm"
vars_cst="${var_cst_z} ${var_cst_lsm}"

inc="1d"
period="19790101_20161231"
model="ERAI"
latbox="30.,60."
lonbox="330.,30."
time="0,3650"

config_file="cyclone_config.json"
list_files="files.txt"

rm -f $list_files

# Get files from B2DROP for this prototype. Later will be directly from a list retrieved from C4I and transferred directly from ESGF
# Construct filenames and specify URLs
# Create text file with url and filenames
#
for i in ${vars_sfc}
do

filename=${i}_${inc}_${period}_${model}.nc

if [ $i = "psl" ]
then
  url="https://b2drop.eudat.eu/s/iseyeocZzZseDCK/download"
fi

echo $url $filename >> $list_files

done

for i in ${vars_500}
do

filename=${i}_${inc}_${period}_${model}.nc

if [ $i = "ua500" ]
then
  url="https://b2drop.eudat.eu/s/mg2mqsLPTop476Z/download"
elif [ $i = "va500" ]
then
  url="https://b2drop.eudat.eu/s/6LCox2SQfG7QxqT/download"
fi

echo $url $filename >> $list_files

done

for i in ${vars_1000}
do

filename=${i}_${inc}_${period}_${model}.nc

if [ $i = "zg1000" ]
then
  url="https://b2drop.eudat.eu/s/DscfqZqKzM6nHBn/download"
fi

echo $url $filename >> $list_files

done

for i in ${vars_cst}
do

filename=${i}_${inc}_${period}_${model}.nc

if [ $i = "z" ]
then
  url="https://b2drop.eudat.eu/s/2cAHx6correNei6/download"
elif [ $i ="lsm" ]
then
  url="https://b2drop.eudat.eu/s/6WzAW8kpcYkq4T3/download"
fi

echo $url $filename >> $list_files

done

# Download files locally
#
cd $WORKDIR/data
$GETFILES $list_files

# Pre-process input files
#
cd $WORKDIR/data
$EXTRACTDATA $list_files $inc $period $model $latbox $lonbox $time

# Calculate tracks
#
cd $WORKDIR/data/results
$TRACKS -i ${period}_${model}.nc -i2 ${var_cst_z}_${model}.nc -i3 ${var_cst_lsm}_${model}.nc -o tracks -getvar ${vars_1000}

python $XMLASCII tracks.xml tracks.txt

#$CREATEMAPS 1000 EUR tracks.txt tracks tracks $BASEMAPDIR

