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

import cf
import numpy as np
import pandas as pd
import read_amo_index as idxamo
import sys
import colorama
from colorama import Fore, Style

YR=int(sys.argv[1:][0])

#Reading the forecasting model 
forecast_model = pd.read_pickle('obs_forecast_model_jan.pkl')

#Previous year minimum
f = np.loadtxt("prev_min.txt", comments="#", delimiter=",", unpack=False)
pmin = f[0] + (f[1]/100)

#Chirps rainfall
chirps = cf.read('chirps-v2.0.'+str(YR-1)+'.nd.mons_p05.nc')[0]
chirps = chirps.subspace(T=cf.year(cf.wi(YR-1,YR))).subspace(X=cf.wi(-85,-33), Y=cf.wi(-40,15)).squeeze()

#Rainfall masks
mask_nov = np.load('mask_chirps_nov.npz')['max_mask_nov']
mask_dec = np.load('mask_chirps_dec.npz')['max_mask_dec']

#Rainfall
rnov = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR-1) & cf.month(11)).squeeze().array)*mask_nov).mean())
rdec = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR-1) & cf.month(12)).squeeze().array)*mask_dec).mean())

rnd = (rnov+rdec)/2.0
rain   = (rnd-forecast_model['Mean'].loc['Rain_ND'])/forecast_model['SD'].loc['Rain_ND']

#Input to data
input_var = np.array([rain, YR, pmin])

#Calculating the forecast
forecast = np.nansum(forecast_model['Coefficients'][1:].values*input_var) + forecast_model['Coefficients'][0]

#Printing forecast
print(Fore.BLUE + str('Forecast for year ')+str(YR)+' = '+format(forecast, '.2f')+'m')
print(Style.RESET_ALL)
