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

def amo_index(SY,EY,MON):

  #Reads in amo vales for SY (Start Year) till EY (End Year) for the MON (Numpy array of Months)
  #from the a txt file called amo.txt downloaded from https://psl.noaa.gov/data/correlation/amon.us.long.data
  #We use the unsmoothed long data version
  #and remove the last lines till only the table end
  #deleted lines
  '''
  -99.99
  AMO unsmoothed from the Kaplan SST V2
  Calculated at NOAA PSL1
  http://www.psl.noaa.gov/data/timeseries/AMO/
  '''
  #description at https://psl.noaa.gov/data/timeseries/AMO/

  #MON can define the months of a season or annual. Should be written in ascending order or the months and should be in the array form
  #For example for NDJFM season, your MON value should be written as: MON = np.array([1,2,3,11,12])
  
  #Following is an example of how to use this definition in your code for deliating the months of NDJFM in the years between 1999-2010:
  
  #import read_amo_index as idx
  #SY = 1999
  #EY = 2010
  #MON = np.array([1,2,3,11,12])
  #amo = idx.amo_index(SY,EY,MON)

  #To just do the seasons instead of the months, you would have to remove the first (1999) J-F-M and the last (2010) N-D months
  #But this cannot be done by this function, you will have to add the index yourself in your script which is something like this:
  #amo = amo[3:-2]
     
  import numpy as np
  import pandas as pd
  
  df = pd.read_table('amo.txt', delim_whitespace=True, header=None, skiprows=1) 
  anom = df.values[:,1:].reshape((df.values.shape[0]*12))
  yrs  = np.repeat(df[0].values, 12)
  mons  = np.tile(np.arange(1,12+1,1), df.values.shape[0])
  anom = anom[(yrs>=SY)&(yrs<=EY)]
  mons  = mons[(yrs>=SY)&(yrs<=EY)]

  if MON.size==1:
    index = anom[(mons==MON[0])]
  if MON.size==2:
    index = anom[(mons==MON[0])|(mons==MON[1])]
  if MON.size==3:
    index = anom[(mons==MON[0])|(mons==MON[1])|(mons==MON[2])]
  if MON.size==4:
    index = anom[(mons==MON[0])|(mons==MON[1])|(mons==MON[2])|(mons==MON[3])]
  if MON.size==5:
    index = anom[(mons==MON[0])|(mons==MON[1])|(mons==MON[2])|(mons==MON[3])|(mons==MON[4])]
  if MON.size==6:
    index = anom[(mons==MON[0])|(mons==MON[1])|(mons==MON[2])|(mons==MON[3])|(mons==MON[4])|(mons==MON[5])]
  if MON.size==7:
    index = anom[(mons==MON[0])|(mons==MON[1])|(mons==MON[2])|(mons==MON[3])|(mons==MON[4])|(mons==MON[5])|(mons==MON[6])]
  if MON.size==8:
    index = anom[(mons==MON[0])|(mons==MON[1])|(mons==MON[2])|(mons==MON[3])|(mons==MON[4])|(mons==MON[5])|(mons==MON[6])|(mons==MON[7])]
  if MON.size==9:
    index = anom[(mons==MON[0])|(mons==MON[1])|(mons==MON[2])|(mons==MON[3])|(mons==MON[4])|(mons==MON[5])|(mons==MON[6])|(mons==MON[7])|(mons==MON[8])]
  if MON.size==10:
    index = anom[(mons==MON[0])|(mons==MON[1])|(mons==MON[2])|(mons==MON[3])|(mons==MON[4])|(mons==MON[5])|(mons==MON[6])|(mons==MON[7])|(mons==MON[8])|(mons==MON[9])]
  if MON.size==11:
    index = anom[(mons==MON[0])|(mons==MON[1])|(mons==MON[2])|(mons==MON[3])|(mons==MON[4])|(mons==MON[5])|(mons==MON[6])|(mons==MON[7])|(mons==MON[8])|(mons==MON[9])|(mons==MON[10])]
  if MON.size==12:
    index = anom[(mons==MON[0])|(mons==MON[1])|(mons==MON[2])|(mons==MON[3])|(mons==MON[4])|(mons==MON[5])|(mons==MON[6])|(mons==MON[7])|(mons==MON[8])|(mons==MON[9])|(mons==MON[10])|(mons==MON[11])]

  return index


