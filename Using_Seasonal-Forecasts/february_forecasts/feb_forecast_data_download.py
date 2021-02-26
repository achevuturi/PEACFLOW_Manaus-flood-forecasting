import cdsapi
import numpy as np
import sys

yr=int(sys.argv[1:][0])

center = 'ecmwf'
mod = 'ecmwf'
mon = 2
sys = 5

var = 'total_precipitation'
c = cdsapi.Client()
c.retrieve(
    'seasonal-monthly-single-levels',
    {
        'format': 'netcdf',
        'originating_centre': center,
        'system': str(sys),
        'year': str(yr),
        'month': str(mon).zfill(2),
        'leadtime_month': ['1','2'],
	'area': [25, -95, -50,-25,],
        'product_type': 'monthly_mean',
        'variable': var,
    },
    mod+'_system'+str(sys)+'_forecast_'+str(yr)+str(mon).zfill(2)+'01_'+var+'_monthly.nc')

var = 'sea_surface_temperature'
c = cdsapi.Client()
c.retrieve(
    'seasonal-monthly-single-levels',
    {
        'format': 'netcdf',
        'originating_centre': center,
        'system': str(sys),
        'year': str(yr),
        'month': str(mon).zfill(2),
        'leadtime_month': ['1','2'],
	'area': [80, -85, -10, 10,],
        'product_type': 'monthly_mean',
        'variable': var,
    },
    mod+'_system'+str(sys)+'_forecast_'+str(yr)+str(mon).zfill(2)+'01_'+var+'_monthly.nc')

