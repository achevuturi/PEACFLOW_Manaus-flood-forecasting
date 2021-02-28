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
chirps = cf.read('chirps-v2.0.'+str(YR-1)+'-'+str(YR)+'.ndj.mons_p05.nc')[0]
chirps = chirps.subspace(T=cf.year(cf.wi(YR-1,YR))).subspace(X=cf.wi(-85,-33), Y=cf.wi(-40,15)).squeeze()

#Rainfall masks
mask_nov = np.load('../mask_chirps_nov.npz')['max_mask_nov']
mask_dec = np.load('../mask_chirps_dec.npz')['max_mask_dec']
mask_jan = np.load('../mask_chirps_jan.npz')['max_mask_jan']

#Rainfall
rnov = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR-1) & cf.month(11)).squeeze().array)*mask_nov).mean())
rdec = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR-1) & cf.month(12)).squeeze().array)*mask_dec).mean())
rjan = (np.ma.masked_invalid((chirps.subspace(T=cf.year(YR) & cf.month(1)).squeeze().array)*mask_jan).mean())

m = np.load('../obs_data.npz')
ch_mfeb = m['mn_feb']
ch_sfeb = m['sd_feb']

mask = np.load('../'+mod+'_mask.npz')['mask']

m = np.load('../'+mod+'_data.npz')
mod_mn_ff=m['mod_mn_ff']
mod_sd_ff=m['mod_sd_ff']
mn_ff=m['mn_ff']
sd_ff=m['sd_ff']

#MODEL
rfeb = np.zeros((ENS));
model = cf.read(mod+'_system'+str(SYS)+'_forecast_'+str(YR)+'0201_total_precipitation_monthly.nc')[0]
model = model.subspace(X=cf.wi(-85,-33), Y=cf.wi(-40,15)).squeeze()
for e in range(ENS):
  rfeb[e] = np.nanmean(((model.subspace(T=cf.month(2)).squeeze().array)[e,:,:])*(mask[3,:,:]))

erfeb = (rfeb-mod_mn_ff)/mod_sd_ff

efeb = np.zeros((erfeb.shape))
for e in range(ENS):
  tfeb = (erfeb[e]*ch_sfeb)+ch_mfeb[0]
  efeb[e] = (rnov+rdec+rjan+tfeb)/4.0

efeb = (efeb-mn_ff)/sd_ff

#Previous year minimum
#dep = cf.read('../water_level_at_manaus.nc')[0]
#pmin = np.nanmin(dep.subspace(T=cf.year(YR-1)).array)
f = np.loadtxt("prev_min.txt", comments="#", delimiter=",", unpack=False)
pmin = f[0] + (f[1]/100)

#Forecast AMO
m = np.load('../'+mod+'_amo.npz')
amo_mn_ff=m['amo_mn_ff']
famo_feb = (calamo.cal_amo_index(mod,SYS,ENS,YR,2,0)) - amo_mn_ff
MON = np.array([1,11,12])
idx = idxamo.amo_index(YR-1,YR,MON)[1:-2]
new = np.zeros((ENS,4))
for e in range(ENS):
  new[e,:] = np.array([idx[0], idx[1], idx[2], famo_feb[e]])
fafeb = np.nanmean(new, axis=1)

forfeb = np.zeros((efeb.shape))
#Input to data
for e in range(ENS):
  input_var = np.array([efeb[e], YR, pmin, fafeb[e]])
  forfeb[e] = np.nansum(forecast_model['Coefficients'][1:].values*input_var) + forecast_model['Coefficients'][0]

forecast = np.nanmean(forfeb, 0)
#Printing forecast
#print(Fore.BLUE + str('Ensemble mean forecast for year ')+str(YR)+' = '+format(forecast, '.2f')+'m')
print(str('Ensemble mean forecast for year ')+str(YR)+' = '+format(forecast, '.2f')+'m')

#Saving ensemble forecast
np.savetxt(str(YR)+'_ensemble_forecast.csv', forfeb, delimiter=',')
#print(Fore.BLUE + str('Saving ensemble forecasts for year ')+str(YR)+' in a csv file')
print(str('Saving ensemble forecasts for year ')+str(YR)+' in a csv file')
#print(Style.RESET_ALL)