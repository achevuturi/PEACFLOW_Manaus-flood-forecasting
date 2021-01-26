import cf
import numpy as np
import pandas as pd
import read_amo_index as idxamo
import sys
import colorama
from colorama import Fore, Style

YR=int(sys.argv[1:][0])

#Reading the forecasting model 
forecast_model = pd.read_pickle('obs_forecast_model_feb.pkl')

#Previous year minimum
dep = cf.read('water_level_at_manaus.nc')[0]
pmin = np.nanmin(dep.subspace(T=cf.year(YR-1)).array)

#AMO
MON = np.array([1,11,12])
amo = np.nanmean(idxamo.amo_index(YR-1,YR,MON)[1:-2])

#Chirps rainfall
chirps = cf.read('chirps-v2.0.'+str(YR-1)+'-'+str(YR)+'.ndj.mons_p05.nc')[0]
chirps = chirps.subspace(T=cf.year(cf.wi(YR-1,YR))).subspace(X=cf.wi(-85,-33), Y=cf.wi(-40,15)).squeeze()

#Rainfall masks
mask_nov = np.load('mask_chirps_nov.npz')['max_mask_nov']
mask_dec = np.load('mask_chirps_dec.npz')['max_mask_dec']
mask_jan = np.load('mask_chirps_jan.npz')['max_mask_jan']

#Rainfall
rnov = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR-1) & cf.month(11)).squeeze().array)*mask_nov).mean())
rdec = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR-1) & cf.month(12)).squeeze().array)*mask_dec).mean())
rjan = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR) & cf.month(1)).squeeze().array)*mask_jan).mean())

rndj = (rnov+rdec+rjan)/3.0
rain   = (rndj-forecast_model['Mean'].loc['Rain_NDJ'])/forecast_model['SD'].loc['Rain_NDJ']

#Input to data
input_var = np.array([rain, YR, amo])

#Calculating the forecast
forecast = np.nansum(forecast_model['Coefficients'][1:].values*input_var) + forecast_model['Coefficients'][0]

#Printing forecast
print(Fore.BLUE + str('Forecast for year ')+str(YR)+' = '+format(forecast, '.2f')+'m')
print(Style.RESET_ALL)
