import numpy as np
import xarray as xr

import numpy as np
import xarray as xr

# Load the ERA5 data
ds_climatology = xr.open_dataset('/Users/joaojesus/Desktop/final_year_proj/samples/2023-04-19-15-15-24.nc')

# Subset the data to the desired sub-region and pressure levels
ds_sub = ds_climatology.sel(latitude=slice(90,30), longitude=slice(-180,180), level=[1,5,10,50,100,200,500])

print('aggregating data')
# Group the data by the day of the year and compute the mean value for each day
climatology = ds_sub.groupby('time.dayofyear').mean(dim='time')

print('saving data')
climatology.to_netcdf('climatology_dayofyear.nc')