#import shutil
import sys
import os
import requests
import numpy as np
import pandas as pd
import xarray as xr

# http://esg1.umr-cnrm.fr/thredds/fileServer/CMIP6_CNRM/ScenarioMIP/CNRM-CERFACS/CNRM-CM6-1/ssp585/r1i1p1f2/day/psl/gr/v20190219/psl_day_CNRM-CM6-1_ssp585_r1i1p1f2_gr_20150101-21001231.nc
# http://esg1.umr-cnrm.fr/thredds/fileServer/CMIP6_CNRM/CMIP/CNRM-CERFACS/CNRM-CM6-1/amip/r1i1p1f2/fx/sftlf/gr/v20181203/sftlf_fx_CNRM-CM6-1_amip_r1i1p1f2_gr.nc

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return local_filename

def get_file_size(url):
    with requests.head(url, allow_redirects=True) as r:
        size = r.headers.get('content-length', -1)
    return size

def check_filecomplete(url, size):
    local_filename = url.split('/')[-1]
    if os.path.exists(local_filename):
        filesize = os.stat(local_filename).st_size
        if filesize != size:
            return False
        else:
            return True
    else:
        return False
    return False

input_file = sys.argv[1]

list_files = open(input_file,"r")

try:
    fil = list_files.readline().rstrip()
    dset = xr.open_dataset(fil)
    dset.close()
except:
    for fil in list_files :
        fil = fil.rstrip()
        filesize = get_file_size(fil)
        if not check_filecomplete(fil, filesize):
            download_file(fil)

list_files.close()
