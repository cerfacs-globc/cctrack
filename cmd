../../../bin/make_tracks.abs -i 19790101_20161231_ERAI.nc -i2 z_ERAI.nc -i3 lsm_ERAI.nc -o tracks -getvar zg1000

python ../../tracking_xml2ascii.py  tracks.xml tracks.txt

../../create_track_maps 1000 EUR tracks.txt /scratch/globc/page/cyclone_tracking/data_era_interim/results/tracks /scratch/globc/page/cyclone_tracking/data_era_interim/results/tracks

