**Flood forecasting for the Negro River at Manaus using observations**

! ----------------------------------------------------------COPYRIGHT----------------------------------------------------------\
! (C) Copyright 2021 University of Reading. All rights reserved.\
! ----------------------------------------------------------COPYRIGHT----------------------------------------------------------\
!\
! This file is part of the CSSP Brazil PEACFLOW Project. \
!\
! Please include the following form of acknowledgement in any presentations/publications\
| that use any of the code stored in this repository:\
! *"The development of PEACFLOW_Manaus-flood-forecasting repository*\
! *(https://github.com/achevuturi/PEACFLOW_Manaus-flood-forecasting)* \
! *was supported by the Newton Fund through the Met Office*\
! *Climate Science for Service Partnership Brazil (CSSP Brazil)*\
! *and was developed at University of Reading."*\
!\
! The CSSP Brazil PEACFLOW Project is free software: you can redistribute it and/or modify\
! it under the terms of the Modified BSD License,\
! as published by the Open Source Initiative.\
!\
! The CSSP Brazil PEACFLOW Project is distributed in the hope that it will be ! useful,\
! but WITHOUT ANY WARRANTY; without even the implied warranty\
! of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the Modified BSD License for more details.\
!\
! For a copy of the Modified BSD License \
! please see <http://opensource.org/licenses/BSD-3-Clause>.\
! -----------------------------------------------------------------------------------------------------------------------------

**Description:**
This module contains models for forecasting maximum water level for the Negro River at Manaus for any year from 2005 onwards using observations as input. This repository has a shell script (.sh) which downloads the required CHIRPS rainfall estimate and executes the flood forecasting model (.pkl) to give the flood forecast for the year requested (.py). There are three different forecast models hosted within the repository, which forecast maximum water level at Manaus at three different lead times: March (obs_forecast_model_mar.sh), February (obs_forecast_model_feb.sh) and January (obs_forecast_model_jan.sh). For any year (2005--current), the forecast models only work after the middle of the month of the forecast, due to the lag in the CHIRPS rainfall uploads.

**Requirements:**
The models hosted in this repository need Python (version3.7; https://www.python.org/downloads/source/) and CDO (version1.9; https://code.mpimet.mpg.de/projects/cdo/). The package also requires installation of the the Python packages: Cf-Python (https://ncas-cms.github.io/cf-python/), Numpy (http://www.numpy.org) and Pandas (https://pandas.pydata.org/)

**Modules:** \
For each forecast model there are three associated files:
- *Shell Script (.sh):* This is the main script that downloads the data, runs the model, gives the output and then deletes the downloaded data.
- *Python Script (.py):* This is the python script that calculated the output using the downloaded data and forecast model information. 
- *Pandas File (.pkl):* This is the statistical forecast model information that is used to calculate the output for each year. 

Names of the three files associated with each forecast model:
- *March:* obs_forecast_model_mar.sh; obs_forecast_model_mar.py; obs_forecast_model_mar.pkl
- *February:* obs_forecast_model_feb.sh; obs_forecast_model_feb.py; obs_forecast_model_feb.pkl
- *January:* obs_forecast_model_jan.sh; obs_forecast_model_jan.py; obs_forecast_model_janr.pkl

Other accessory files are:
- *water_level_at_manaus.nc:* NetCDF file for historical water level for Negro River at Manaus to get previous year's minimum level.
- *read_amo_index.py:* Python script to read the AMO index from the downloaded amo.txt to get monthly AMO index. 
- *max_chirps_???.npz:* Numpy output files which have CHIRPS monthly rainfall masks for November (max_chirps_nov.npz), December (max_chirps_dec.npz), January (max_chirps_jan.npz), February (max_chirps_feb.npz)

**Execution:**
The model works by running the shell scripts of the month which needs the forecast using the example command below: 
**./obs_forecast_model_mar.sh** OR **source obs_forecast_model_mar.sh**

After this command, the user needs to provide the year for which the forecast is required (2005 onwards) when prompted by the script to complete the run. 
1. For the forecasts to be **issued in March** use **./obs_forecast_model_mar.sh** OR **source obs_forecast_model_mar.sh** 
2. For the forecasts to be **issued in February** use **./obs_forecast_model_feb.sh** OR **source obs_forecast_model_feb.sh** 
3. For the forecasts to be **issued in January** use **./obs_forecast_model_jan.sh** OR **source obs_forecast_model_jan.sh** 

**Output:**
The forecast of the maximum water level of Negro River at Manaus (in meters) is given in the command line. All the downloaded data (CHIRPS rainfall and AMO index text file) is then deleted.

**Citation:**
Users who apply the code resulting in presentations/publications are kindly asked to cite the publication below:\
*Chevuturi A, Klingaman NP, Rudorff CM, Coelho CAS, Schongart J (2021) Forecasting annual maximum water level for the Negro River at Manaus. Climate Resilience and Sustainability, submitted.*
