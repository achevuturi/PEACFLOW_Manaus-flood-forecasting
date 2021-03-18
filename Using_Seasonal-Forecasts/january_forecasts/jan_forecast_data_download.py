'''
! ----------------------------------------------------------COPYRIGHT----------------------------------------------------------
! (C) Copyright 2021 University of Reading. All rights reserved.
! ----------------------------------------------------------COPYRIGHT----------------------------------------------------------
!
! This file is part of the CSSP Brazil PEACFLOW Project. 
!
! Please include the following form of acknowledgement in any presentations/publications
| that use any of the code stored in this repository:
! "The development of PEACFLOW_Manaus-flood-forecasting repository 
! (https://github.com/achevuturi/PEACFLOW_Manaus-flood-forecasting)
! was supported by the Newton Fund through the Met Office 
! Climate Science for Service Partnership Brazil (CSSP Brazil) 
! and was developed at University of Reading."
!
! The CSSP Brazil PEACFLOW Project is free software: you can redistribute it and/or modify
! it under the terms of the Modified BSD License,
! as published by the Open Source Initiative.
!
! The CSSP Brazil PEACFLOW Project is distributed in the hope that it will be ! useful,
! but WITHOUT ANY WARRANTY; without even the implied warranty
! of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the Modified BSD License for more details.
!
! For a copy of the Modified BSD License 
! please see <http://opensource.org/licenses/BSD-3-Clause>.
! -----------------------------------------------------------------------------------------------------------------------------
'''

import cdsapi
import numpy as np
import sys

yr=int(sys.argv[1:][0])

center = 'ecmwf'
mod = 'ecmwf'
mon = 1
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

