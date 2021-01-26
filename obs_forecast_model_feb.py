import cf
import numpy as np
import pandas as pd
import read_amo_index as idxamo
import sys
import colorama
from colorama import Fore, Style

YR=int(sys.argv[1:][0])
#YR = 2020

#Reading the forecasting model 
forecast_model = pd.read_pickle('obs_forecast_model_feb.pkl')

#Previous year minimum
dep = cf.read('water_level_at_manaus.nc')[0]
pmin = np.nanmin(dep.subspace(T=cf.year(YR-1)).array)
#dep_min = np.nanmin(dep.subspace(T=cf.year(YR-1)).array)
#pmin = (dep_min-forecast_model['Mean'].loc['Prev_Min'])/forecast_model['SD'].loc['Prev_Min']

#AMO
MON = np.array([1,11,12])
amo = np.nanmean(idxamo.amo_index(YR-1,YR,MON)[1:-2])
#idx = np.nanmean(idxamo.amo_index(YR-1,YR,MON)[2:-2])
#amo = (idx-forecast_model['Mean'].loc['AMO'])/forecast_model['SD'].loc['AMO']

#Chirps rainfall
chirps = cf.read('chirps-v2.0.'+str(YR-1)+'-'+str(YR)+'.ndj.mons_p05.nc')[0]
#chirps = cf.read('/gws/nopw/j04/ncas_climate_vol1/users/amulya/data/obs/prcp/chirps/chirps-v2.0.1981-2020.mons_p05_Brazil.nc')[0]
chirps = chirps.subspace(T=cf.year(cf.wi(YR-1,YR))).subspace(X=cf.wi(-85,-33), Y=cf.wi(-40,15)).squeeze()
mask_three = cf.read('/gws/nopw/j04/klingaman/amulya/data/peacflow/river_catchments_shapefiles/All_Three.nc')[0].subspace(X=cf.wi(-85,-33), Y=cf.wi(-40,15)).squeeze()

#Rainfall masks
m = np.load('mask_chirps.npz')
corr = m['max_corr']
pval = m['max_pval']
sign = corr.copy()
sign[(pval>0.05) | (sign<=0)] = np.nan
mask = sign.copy()
mask[~np.isnan(sign)] = 1.0
mask_o = mask.copy()
for i in range(5):
  mask_o[i,:,:][(mask[i,:,:]!=1.0) | (mask_three.array!=1.0)] = np.nan

rnov = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR-1) & cf.month(11)).squeeze().array)*mask_o[0,:,:]).mean())
rdec = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR-1) & cf.month(12)).squeeze().array)*mask_o[1,:,:]).mean())
rjan = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR) & cf.month(1)).squeeze().array)*mask_o[2,:,:]).mean())

rndj = (rnov+rdec+rjan)/3.0
rain   = (rndj-forecast_model['Mean'].loc['Rain_NDJ'])/forecast_model['SD'].loc['Rain_NDJ']

#Input to data
input_var = np.array([rain, YR, amo])

#Calculating the forecast
forecast = np.nansum(forecast_model['Coefficients'][1:].values*input_var) + forecast_model['Coefficients'][0]

#Printing forecast
print(Fore.BLUE + str('Forecast for year ')+str(YR)+' = '+format(forecast, '.2f')+'m')
print(Style.RESET_ALL)
