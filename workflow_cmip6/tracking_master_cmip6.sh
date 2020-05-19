#!/bin/sh -vx
#
TRACKDIR="$1"
WORKDIR="$2"
CONFIGFILE="$3"

# Tracking package directory
if [ -z $TRACKDIR ]
then
  echo "TRACKDIR argument 1 is missing."
  exit 1
fi
if [ ! -d $TRACKDIR ]
then
  echo "Directory $TRACKDIR does not exist."
  exit 1
fi

# Working directory
if [ -z $WORKDIR ]
then
  echo "WORKDIR argument 2 is missing."
  exit 1
fi
if [ ! -d $WORKDIR ]
then
  echo "Directory $WORKDIR does not exist."
  exit 1
fi

# Configuration file
if [ -z $CONFIGFILE ]
then
  echo "CONFIGFILE argument 3 is missing."
  exit 1
fi
if [ ! -s $CONFIGFILE ]
then
  echo "Configuration file $CONFIGFILE does not exist."
  exit 1
fi


export PATH=${PATH}:${TRACKDIR}

# Executables
EXTRACTDATA=${TRACKDIR}/extractnc.py
TRACKS=${TRACKDIR}/make_tracks.abs
XMLASCII=${TRACKDIR}/tracking_xml2ascii.py
CONCATFILES=${TRACKDIR}/ConcatenationFichiers.py
CREATEMAPS=${TRACKDIR}/main_cartes.py
PROCESSFILES=${TRACKDIR}/processfiles.py
TRANSFERFILES=${TRACKDIR}/transferfiles.py

if [ ! -s $EXTRACTDATA ]
then
  echo "$EXTRACTDATA is missing."
  exit 1
fi
if [ ! -s $TRACKS ]
then
  echo "$TRACKS is missing."
  exit 1
fi
if [ ! -s $XMLASCII ]
then
  echo "$XMLASCII is missing."
  exit 1
fi
if [ ! -s $CONCATFILES ]
then
  echo "$CONCATFILES is missing."
  exit 1
fi
if [ ! -s $CREATEMAPS ]
then
  echo "$CREATEMAPS is missing."
  exit 1
fi

# Create data directory if it does not exist
datadir=$WORKDIR/data
if [ -d $datadir ]
then
  echo "$datadir already exists. Using existing directory."
else
  mkdir $datadir
fi

# Create results directory if it does not exist
resultsdir=$datadir/results
if [ -d $resultsdir ]
then
  echo "$resultsdir already exists. Using existing directory."
else
  mkdir $resultsdir
fi

# Remove warmstart.txt if it exists
warmstart=$resultsdir/warmstart.txt
rm -f $warmstart


#### CONFIG for CMIP6 data
####
psl="psl"
orog="orog"
ua500="ua"
va500="va"
zg1000="zg"
lsm="sftlf"

latmin="30.0"
latmax="40.0"
lonmin="10.0"
lonmax="20.0"
period_start_date="20500101"
period_end_date="20511231"
period=${period_start_date}-${period_end_date}

curdir=`pwd`

configfile=$CONFIGFILE
out_file="tracks.txt"
list_files="${curdir}/input_files.txt"
list_sel_files="input_selected_files.txt"
list_tracks="input_tracks.txt"

rm -f $WORKDIR/data/results/$list_tracks

# From list of files provided, check that all needed input data is provided, and select needed files according to time period
#
cd $WORKDIR/data
python $PROCESSFILES $list_files $list_sel_files $period_start_date $period_end_date $psl $zg1000 $ua500 $va500 $orog $lsm

# Transfer files if not using OpenDAP
#
cd $WORKDIR/data
python $TRANSFERFILES $list_sel_files

# Subsetting and pre-process input files
#
cd $WORKDIR/data
python $EXTRACTDATA $list_sel_files $latmin $latmax $lonmin $lonmax $period_start_date $period_end_date $psl $zg1000 $ua500 $va500 $orog $lsm

# Calculate tracks
#
cd $WORKDIR/data/results

line=`grep ${psl}_ ${list_files} | head -n 1`
filename=`basename $line`
model=`echo $filename | awk 'BEGIN {FS="_"} {print $3}'`

ls -l ${model}_${period}.nc ${orog}*.nc ${lsm}*.nc

$TRACKS -i ${model}_${period}.nc -i2 ${orog}*.nc -i3 ${lsm}*.nc -o tracks -getvar zg -configfile $configfile 

python $XMLASCII tracks.xml tracks_${period}.txt

rm -f $warmstart

# Create file warmstart.txt to start next tracking in "Mode Warmstart"
#
 
d=`awk 'END {print $7}' tracks_${period}.txt`
m=`awk 'END {print $8}' tracks_${period}.txt`
y=`awk 'END {print $9}' tracks_${period}.txt`

awk -v day=$d -v month=$m -v year=$y '$7==day && $8==month && $9==year {print $2,$3}' tracks_${period}.txt >> $warmstart 

#Create input_file with filenames of tracks_period.txt
#

echo "tracks_${period}.txt" >> $list_tracks

exit 0

#cd $WORKDIR/data/results
#python $CONCATENATEFILES $list_tracks $out_file


#python $CREATEMAPS $out_file
