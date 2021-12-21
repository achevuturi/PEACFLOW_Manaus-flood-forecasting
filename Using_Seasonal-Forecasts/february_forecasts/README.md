
**Flood forecasting for Negro River at Manaus using seasonal forecasts for February lead-time**

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
This module contains models for forecasting maximum water level for Negro River at Manaus for any year from 2017 onwards using combination of observations and ECMWF seasonal forecasts as input. The required input data files are available in the parent directory (https://github.com/achevuturi/PEACFLOW_Manaus-flood-forecasting/tree/master/Using_Seasonal-Forecasts). This sub-folder has one model that provides forecasts at February lead-time for each year. 

**Modules:** This sub-folder contains the following files:
- *calculate_amo_index.py:* Python script that calculates the ECMWF AMO index from the downloaded ECMWF SST forecast NetCDF file.
- *read_amo_index.py:* Python script to read the AMO index from the downloaded amo.txt to get monthly AMO index (as in https://github.com/achevuturi/PEACFLOW_Manaus-flood-forecasting/tree/master/Using_Observations)
- *feb_forecast_data_download.py:* Python script that downloads the ECMWF February forecast of the year of forecast over Amazon region. This script downloads two NetCDF files, one for total-precipitation and another for sea-surface-temperature. 
- *model_uncertainity.py:* Python script that calculates the model uncertanity for the forecast provided using whole ensemble forecast. The scale for the model uncertanity is derived from the errors over the validation period. - *feb_forecast_output.py:* Python script that calculates the output using the downloaded observed and ECMWF forecast data and model information (https://github.com/achevuturi/PEACFLOW_Manaus-flood-forecasting/blob/master/Using_Seasonal-Forecasts/obs_forecast_model_mar.pkl). It also uses data from the numpy files; .npz, stored in https://github.com/achevuturi/PEACFLOW_Manaus-flood-forecasting/tree/master/Using_Seasonal-Forecasts.
- *feb_forecast.sh:* This is the main script that downloads the data, runs the model, gives/saves the output and then deletes the downloaded data.

**Execution:** The model works by running the shell script for the forecast using the example command **bash feb_forecast.sh** OR **./feb_forecast.sh** OR **source feb_forecast.sh**. After this command, the user needs to provide the year for which the forecast is required (2017 onwards) when prompted by the script to complete the run. The first step of this model is to delete any old ensemble forecasts saved as a .csv file.

**Output:**
The esemble mean forecast of the maximum water level of Negro River at Manaus (in meters) is given in the command line, and the ensemble forecast is saved as an output .csv file. The uncertainity bounds of the forecast (5<sup>th</sup> -- 95<sup>th</sup> percentile range) are also printed out. All the downloaded data is then deleted.

**Citation:**
Users who apply the code resulting in presentations/publications are kindly asked to cite the publication below:\
*Chevuturi A, Klingaman NP, Woolnough SJ, Rudorff CM, Coelho CAS, Schongart J (2021) Extending forecast lead time for annual maximum water level at Manaus using seasonal forecasts. Climate Resilience and Sustainability, in prep.*
