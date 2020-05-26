import shutil
import sys
import os
import numpy as np
import pandas as pd
import xarray as xr

input_file = sys.argv[1]
minlat = float(sys.argv[2])
maxlat = float(sys.argv[3])
minlon = float(sys.argv[4])
maxlon = float(sys.argv[5])
period_start_time = sys.argv[6]
period_end_time = sys.argv[7]
psl = sys.argv[8]
zg1000 = sys.argv[9]
ua500 = sys.argv[10]
va500 = sys.argv[11]
orog = sys.argv[12]
lsm = sys.argv[13]

f = open(input_file,"r")
allfiles=f.readlines()

for f in allfiles:
  f.rstrip()
  fb = f.rsplit('/', 1)[-1]
  fbs = fb.strip('.nc')
  params = fbs.split('_',-1)
  varname = params[0]

  if varname == psl:    
     model = params[2]
     break

outfilenc=model+"_"+period_start_time+'-'+period_end_time+".nc"

year_start = int(period_start_time[0:4])
month_start = int(period_start_time[4:6])
day_start = int(period_start_time[6:8])
starttime = str(year_start)+"-"+str(month_start)+"-"+str(day_start)

year_end = int(period_end_time[0:4])
month_end = int(period_end_time[4:6])
day_end = int(period_end_time[6:8])
endtime = str(year_end)+"-"+str(month_end)+"-"+str(day_end)

if not( os.path.isdir('results')):
   os.mkdir('results')

if os.path.isfile('results/'+outfilenc):
   os.remove('results/'+outfilenc)

files = []
for f in allfiles:

   f = f.rstrip()
   print(f)
   dset = xr.open_dataset(f, mask_and_scale=False, decode_times=True, decode_coords=True)
   try:
     del dset.attrs['_NCProperties']
   except:
     pass

   fb = f.rsplit('/', 1)[-1]
   params = fb.split('_',-1)
   var = params[0]
   print(var)
   if minlon > maxlon or minlon < 0:
     if var == ua500 or var == va500 or var == zg1000 :
       level=500.0
       dset = dset.sel(time=slice(starttime,endtime), plev=slice(level*100,level*100), lat=slice(minlat,maxlat)).squeeze(dim=None, drop=True)
     elif var == psl :
       dset = dset.sel(time=slice(starttime,endtime), lat=slice(minlat,maxlat))
     else :
       dset = dset.sel(lat=slice(minlat,maxlat))
   else:
     if var == ua500 or var == va500 or var == zg1000 :
       level=500.0
       dset = dset.sel(time=slice(starttime,endtime), plev=slice(level*100,level*100), lon=slice(minlon,maxlon), lat=slice(minlat,maxlat)).squeeze(dim=None, drop=True)
     elif var == psl :
       dset = dset.sel(time=slice(starttime,endtime), lon=slice(minlon,maxlon), lat=slice(minlat,maxlat))
     else :
       dset = dset.sel(lon=slice(minlon,maxlon), lat=slice(minlat,maxlat))

   print("Saving to: "+"results/"+fb)
   dims = dset.dims
   dimsf = {k: v for k, v in dims.items() if k.startswith('lat') or k.startswith('lon') or k.startswith('time')}
   enc = dict(dimsf)
   enc = dict.fromkeys(enc, {'_FillValue': None})

   if var == orog or var == lsm :
      dset.to_netcdf(path="results/"+fb, mode='w', format='NETCDF4', encoding=enc)
   else:
      files.append("results/"+fb)
      dset.to_netcdf(path="results/"+fb, mode='w', format='NETCDF4', unlimited_dims='time', encoding=enc)
      tunits = dset.time.encoding['units']

   dset.close()
   del dset

# Reorder longitudes if needed, and subset longitudes in that specific case differently (need to do it on local file for reasonable performance)
   if minlon > maxlon or minlon < 0:
     print("Subsetting for non-contiguous longitude")
     dsetl = xr.open_dataset("results/"+fb, mask_and_scale=False, decode_times=True, decode_coords=True)
     saveattrs = dsetl.lon.attrs
#     dsetl = dsetl.assign_coords(lon=(((dsetl.lon + 180) % 360) - 180)).roll(lon=(-dsetl.lon.searchsorted(minlon)), roll_coords=True)
#     dsetl = dsetl.assign_coords(lon=(dsetl.lon % 360)).roll(lon=(dsetl.dims['lon'] // 2))
     dsetl = dsetl.assign_coords(lon=(((dsetl.lon + 180) % 360) - 180)).roll(lon=(dsetl.dims['lon'] // 2), roll_coords=True)
     if minlon >= 180:
       minlon = minlon - 360
     if maxlon >= 180:
       maxlon = maxlon - 360
     dsetl = dsetl.sel(lon=slice(minlon,maxlon))
     #     dsetl = dsetl.sel(lon=(dset.lon <= maxlon) | (dset.lon >= minlon))
     dsetl.lon.attrs = saveattrs
     if var == orog or var == lsm :
       dsetl.to_netcdf(path="results/tmp"+fb, mode='w', format='NETCDF4', encoding=enc)
     else :
       dsetl.time.encoding['units'] = tunits
       dsetl.to_netcdf(path="results/tmp"+fb, mode='w', format='NETCDF4', unlimited_dims='time', encoding=enc)
     dsetl.close()
     del dsetl
     os.rename("results/tmp"+fb, "results/"+fb)

# Combine all files into one
dsmerged = xr.open_mfdataset(files, mask_and_scale=False, decode_times=True, decode_coords=True, combine='by_coords')
print("Merging files into: "+"results/"+outfilenc)
print(files)
dsmerged.to_netcdf(path="results/"+outfilenc, mode='w', format='NETCDF4', unlimited_dims='time')
