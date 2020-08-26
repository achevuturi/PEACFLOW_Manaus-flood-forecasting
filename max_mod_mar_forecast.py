from __future__ import division
import cf, cfplot as cfp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
import read_amo_index as idxamo
import sys

YR=int(sys.argv[1:][0])

#Reading the forecasting model 
forecast_model = pd.read_pickle('forecast_model.pkl')

#Previous year minimum
dep = cf.read('water_level_at_manaus.nc')[0]
dep_min = np.nanmin(dep.subspace(T=cf.year(YR-1)).array)
pmin = (dep_min-forecast_model['Mean'].loc['Prev_Min'])/forecast_model['SD'].loc['Prev_Min']


#AMO
MON = np.array([1,2,11,12])
idx = np.nanmean(idxamo.amo_index(YR-1,YR,MON)[2:-2])
amo = (idx-forecast_model['Mean'].loc['AMO'])/forecast_model['SD'].loc['AMO']


#Chirps rainfall
chirps = cf.read('chirps-v2.0.'+str(YR-1)+'-'+str(YR)+'.ndjf.mons_p05.nc')[0]
chirps = chirps.subspace(T=cf.year(cf.wi(YR-1,YR))).subspace(X=cf.wi(-85,-33), Y=cf.wi(-40,15)).squeeze()
mask_three = cf.read('/gws/nopw/j04/klingaman/amulya/data/peacflow/river_catchments_shapefiles/All_Three.nc')[0].subspace(X=cf.wi(-85,-33), Y=cf.wi(-40,15)).squeeze()

#Rainfall masks
m = np.load('../corr/mask_chirps.npz')
corr = m['max_corr']
pval = m['max_pval']
sign = corr.copy()
sign[(pval>0.05) | (sign<=0)] = np.nan
mask = sign.copy()
mask[~np.isnan(sign)] = 1.0
mask_o = mask.copy()
for i in range(24):
  mask_o[i,:,:][(mask[i,:,:]!=1.0) | (mask_three.array!=1.0)] = np.nan

rnov = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR-1) & cf.month(11)).squeeze().array)*mask_o[10,:,:]).mean())
rdec = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR-1) & cf.month(12)).squeeze().array)*mask_o[11,:,:]).mean())
rjan = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR) & cf.month(1)).squeeze().array)*mask_o[12,:,:]).mean())
rfeb = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR) & cf.month(2)).squeeze().array)*mask_o[13,:,:]).mean())

rndjf = (rnov+rdec+rjan+rfeb)/4.0
rain   = (rndjf-forecast_model['Mean'].loc['Rain_NDJF'])/forecast_model['SD'].loc['Rain_NDJF']

#Input to data
input_var = np.array([rain, YR, pmin, amo])

#Calculating the forecast
forecast = np.nansum(forecast_model['Coefficients'][1:].values*input_var) + forecast_model['Coefficients'][0]
print(str('Forecast for year ')+str(YR)+' = '+format(forecast, '.2f')+'m')

#print(forecast)

