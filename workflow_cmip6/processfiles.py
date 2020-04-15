#import shutil
import sys
import os
import datetime 

input_file = sys.argv[1]
output_file = sys.argv[2]
period_start_date = sys.argv[3]
period_end_date = sys.argv[4]
psl = sys.argv[5]
zg1000 = sys.argv[6]
ua500 = sys.argv[7]
va500 = sys.argv[8]
orog = sys.argv[9]
lsm = sys.argv[10]

# http://esg1.umr-cnrm.fr/thredds/fileServer/CMIP6_CNRM/ScenarioMIP/CNRM-CERFACS/CNRM-CM6-1/ssp585/r1i1p1f2/day/psl/gr/v20190219/psl_day_CNRM-CM6-1_ssp585_r1i1p1f2_gr_20150101-21001231.nc
# http://esg1.umr-cnrm.fr/thredds/fileServer/CMIP6_CNRM/CMIP/CNRM-CERFACS/CNRM-CM6-1/amip/r1i1p1f2/fx/sftlf/gr/v20181203/sftlf_fx_CNRM-CM6-1_amip_r1i1p1f2_gr.nc


list_files= open(input_file,"r")

outf = open(output_file, "w")

for fil in list_files :

   fil = fil.rstrip()

   filb = fil.rsplit('/', 1)[-1]
   filbs = filb.strip('.nc')

   params = filbs.split('_',-1)
   
   varname = params[0]
   interval = params[1]
   model = params[2]
   scenario = params[3]
   experiment = params[4]
   grid = params[5]
   if varname != orog and varname != lsm:
      period = params[6]

      periods = period.split('-')
      period_start = periods[0]
      period_end = periods[1]

      year_startf = int(period_start[0:4])
      month_startf = int(period_start[4:6])
      day_startf = int(period_start[6:8])
      
      startf = datetime.datetime(year_startf, month_startf, day_startf)
   
      year_endf = int(period_end[0:4])
      month_endf = int(period_end[4:6])
      day_endf = int(period_end[6:8])

      endf = datetime.datetime(year_endf, month_endf, day_endf)

      year_start = int(period_start_date[0:4])
      month_start = int(period_start_date[4:6])
      day_start = int(period_start_date[6:8])

      start = datetime.datetime(year_start, month_start, day_start)

      year_end = int(period_end_date[0:4])
      month_end = int(period_end_date[4:6])
      day_end = int(period_end_date[6:8])

      end = datetime.datetime(year_end, month_end, day_end)

      if start <= endf and end >= startf:
         print(fil)
         outf.write(fil + '\n')

   else:
      print('lsm or orog:  : '+fil)
      outf.write(fil + '\n')

list_files.close()
outf.close()

