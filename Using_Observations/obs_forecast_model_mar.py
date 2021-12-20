import cf
import numpy as np
import pandas as pd
from scipy.stats import norm
import read_amo_index as idxamo
import sys
from colorama import Fore, Style

YR=int(sys.argv[1:][0])

#Reading the forecasting model 
forecast_model = pd.read_pickle('obs_forecast_model_mar.pkl')

#Previous year minimum
f = np.loadtxt("prev_min.txt", comments="#", delimiter=",", unpack=False)
pmin = f[0] + (f[1]/100)

#AMO
MON = np.array([1,2,11,12])
amo = np.nanmean(idxamo.amo_index(YR-1,YR,MON)[2:-2])

#Chirps rainfall
chirps = cf.read('chirps-v2.0.'+str(YR-1)+'-'+str(YR)+'.ndjf.mons_p05.nc')[0]
chirps = chirps.subspace(T=cf.year(cf.wi(YR-1,YR))).subspace(X=cf.wi(-85,-33), Y=cf.wi(-40,15)).squeeze()

#Rainfall masks
mask_nov = np.load('mask_chirps_nov.npz')['max_mask_nov']
mask_dec = np.load('mask_chirps_dec.npz')['max_mask_dec']
mask_jan = np.load('mask_chirps_jan.npz')['max_mask_jan']
mask_feb = np.load('mask_chirps_feb.npz')['max_mask_feb']

#Rainfall
rnov = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR-1) & cf.month(11)).squeeze().array)*mask_nov).mean())
rdec = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR-1) & cf.month(12)).squeeze().array)*mask_dec).mean())
rjan = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR) & cf.month(1)).squeeze().array)*mask_jan).mean())
rfeb = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR) & cf.month(2)).squeeze().array)*mask_feb).mean())

rndjf = (rnov+rdec+rjan+rfeb)/4.0
rain   = (rndjf-forecast_model['Mean'].loc['Rain_NDJF'])/forecast_model['SD'].loc['Rain_NDJF']

#Input to data
input_var = np.array([rain, YR, pmin, amo])

#Calculating the forecast
forecast = np.nansum(forecast_model['Coefficients'][1:-1].values*input_var) + forecast_model['Coefficients'][0]

#Calculate uncertainity (5th to 95th percentile)
bounds = (0.05, 0.95)
uc05, uc95 = (norm.ppf(bounds[0], loc=forecast, scale=forecast_model['SD']['Error']),
              norm.ppf(bounds[1], loc=forecast, scale=forecast_model['SD']['Error']))

#Printing forecast and uncertainity
print(Fore.BLUE + str('Forecast for year ')+str(YR)+' = '+format(forecast, '.2f')+'m')
print(Fore.BLUE + str('Uncertainity (5th -- 95th percentile) = ')+format(uc05, '.2f')+'m -- '+format(uc95, '.2f')+'m')
print(Style.RESET_ALL)
