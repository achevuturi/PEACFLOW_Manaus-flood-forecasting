def cal_amo_index(data,sys,ENS,YR,MON,LEAD):
  '''
  Need to give the name of the data in string format
  Then system (sys), ensemble member (ENS), start year (SY), end year (EY), 
  and then month of forecast (MON) and which lead month (LEAD)
  e.g.:

  data = 'ecmwf'
  sys = 5
  MON = 1
  SY = 1994
  EY = 2016
  ENS = 25
  LEAD = 0

  Function writes out the amo index for the seasonal reforecasts for all ensemble members
  #AMO region is 0N to 70N and 75W to 5 E.
  '''

  import numpy as np
  import cf, cfplot as cfp

  filename = data+'_system'+str(sys)+'_forecast_'+str(YR)+str(MON).zfill(2)+'01_sea_surface_temperature_monthly.nc'
  f = cf.read(filename)[0]
  f = f.subspace(X=cf.wi(-75,0), Y=cf.wi(0,70)).collapse('area: mean').squeeze()
  amo = f.subspace[LEAD,:].array.squeeze() 

  return amo

