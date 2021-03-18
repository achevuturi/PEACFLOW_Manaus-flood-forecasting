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
import calculate_amo_index as calamo
import sys
#import colorama
#from colorama import Fore, Style

YR=int(sys.argv[1:][0])
#YR = 2020

mod = 'ecmwf'
ENS=51
SYS=5

#Reading the forecasting model 
forecast_model = pd.read_pickle('../obs_forecast_model_mar.pkl')

#Chirps rainfall
chirps = cf.read('chirps-v2.0.'+str(YR-1)+'-'+str(YR)+'.nd.mons_p05.nc')[0]
chirps = chirps.subspace(T=cf.year(cf.wi(YR-1,YR))).subspace(X=cf.wi(-85,-33), Y=cf.wi(-40,15)).squeeze()

#Rainfall masks
mask_nov = np.load('../mask_chirps_nov.npz')['max_mask_nov']
mask_dec = np.load('../mask_chirps_dec.npz')['max_mask_dec']

#Rainfall
rnov = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR-1) & cf.month(11)).squeeze().array)*mask_nov).mean())
rdec = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR-1) & cf.month(12)).squeeze().array)*mask_dec).mean())

m = np.load('../obs_data.npz')
ch_mjan = m['mn_jan']
ch_sjan = m['sd_jan']
ch_mfeb = m['mn_feb']
ch_sfeb = m['sd_feb']

mask = np.load('../'+mod+'_mask.npz')['mask']

m = np.load('../'+mod+'_data.npz')
mod_mn_jf=m['mod_mn_jf']
mod_sd_jf=m['mod_sd_jf']
mod_mn_jj=m['mod_mn_jj']
mod_sd_jj=m['mod_sd_jj']
mn_jj=m['mn_jj']
sd_jj=m['sd_jj']

#MODEL
rjan = np.zeros((ENS)); rfeb = np.zeros((ENS));
model = cf.read(mod+'_system'+str(SYS)+'_forecast_'+str(YR)+'0101_total_precipitation_monthly.nc')[0]
model = model.subspace(X=cf.wi(-85,-33), Y=cf.wi(-40,15)).squeeze()
for e in range(ENS):
 rjan[e] = np.nanmean(((model.subspace(T=cf.month(1)).squeeze().array)[e,:,:])*(mask[2,:,:]))
 rfeb[e] = np.nanmean(((model.subspace(T=cf.month(2)).squeeze().array)[e,:,:])*(mask[3,:,:]))

erjan = (rjan-mod_mn_jj)/mod_sd_jj
erfeb = (rfeb-mod_mn_jf)/mod_sd_jf

ejan = np.zeros((erjan.shape))
for e in range(ENS):
  tjan = (erjan[e]*ch_sjan)+ch_mjan[0]
  tfeb = (erfeb[e]*ch_sfeb)+ch_mfeb[0]
  ejan[e] = (rnov+rdec+tjan+tjan)/4.0

ejan = (ejan-mn_jj)/sd_jj

#Previous year minimum
f = np.loadtxt("prev_min.txt", comments="#", delimiter=",", unpack=False)
pmin = f[0] + (f[1]/100)

#Forecast AMO
m = np.load('../'+mod+'_amo.npz')
amo_mn_jj=m['amo_mn_jj']
amo_mn_jf=m['amo_mn_jf']
famo_jan = (calamo.cal_amo_index(mod,SYS,ENS,YR,1,0)) - amo_mn_jj
famo_feb = (calamo.cal_amo_index(mod,SYS,ENS,YR,1,1)) - amo_mn_jf
MON = np.array([11,12])
idx = idxamo.amo_index(YR-1,YR,MON)[:-2]
new = np.zeros((ENS,4))
for e in range(ENS):
  new[e,:] = np.array([idx[0], idx[1], famo_jan[e], famo_feb[e]])
fajan = np.nanmean(new, axis=1)

forjan = np.zeros((ejan.shape))
#Input to data
for e in range(ENS):
  input_var = np.array([ejan[e], YR, pmin, fajan[e]])
  forjan[e] = np.nansum(forecast_model['Coefficients'][1:].values*input_var) + forecast_model['Coefficients'][0]

forecast = np.nanmean(forjan, 0)
#Printing forecast
#print(Fore.BLUE + str('Ensemble mean forecast for year ')+str(YR)+' = '+format(forecast, '.2f')+'m')
print(str('Ensemble mean forecast for year ')+str(YR)+' = '+format(forecast, '.2f')+'m')

#Saving ensemble forecast
np.savetxt(str(YR)+'_ensemble_forecast.csv', forjan, delimiter=',')
#print(Fore.BLUE + str('Saving ensemble forecasts for year ')+str(YR)+' in a csv file')
print(str('Saving ensemble forecasts for year ')+str(YR)+' in a csv file')
#print(Style.RESET_ALL)
