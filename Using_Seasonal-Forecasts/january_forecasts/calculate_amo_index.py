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

