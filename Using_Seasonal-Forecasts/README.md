**Flood forecasting for the Negro River at Manaus using seasonal forecasts**

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
This module contains models for forecasting maximum water level for the Negro River at Manaus for any year from 2017 onwards using combination of observations and ECMWF seasonal forecasts as input. This repository has required data files that are used to run the forecast models and the forecast models in sub-folders. There are two models within this module that provide forecasts at January and February lead-time. For more details about the models and their execution please read the README.md files contained within each sub-folders.  

**Requirements:**
The models hosted in this repository need Python (version3.7; https://www.python.org/downloads/source/) and CDO (version1.9; https://code.mpimet.mpg.de/projects/cdo/). The package also requires installation of the Python packages: Cf-Python (https://ncas-cms.github.io/cf-python/), Numpy (http://www.numpy.org), Pandas (https://pandas.pydata.org/) and CDSAPI (https://cds.climate.copernicus.eu/api-how-to)

**Modules:**
For each forecast model there is one sub-folder:
- *february_forecasts:* This sub-folder for executing the model to get flood forecasts at February lead-time of each year. 
- *january_forecasts:*  This sub-folder for executing the model to get flood forecasts at January lead-time of each year. -

Other accessory files within this module are required data files to execute the forecast models:
- *ecmwf_amo.npz:* Numpy output file which contains ECMWF seasonal forecast AMO input data standardization information.
- *obs_data.npz:* Numpy output file which contains observed rainfall input data standardization information.
- *ecmwf_data.npz:* Numpy output file which contains ECMWF seasonal forecast rainfall input data standardization information.
- *max_chirps_???.npz:* Numpy output files which have CHIRPS monthly rainfall masks for November (max_chirps_nov.npz), December (max_chirps_dec.npz), January (max_chirps_jan.npz) (as in https://github.com/achevuturi/PEACFLOW_Manaus-flood-forecasting/tree/master/Using_Observations).
- *ecmwf_mask.npz:* Numpy output file which has ECMWF monthly rainfall masks for January and February, regridded from CHIRPS monthly rainfall masks.
- *obs_forecast_model_mar.pkl:* This is the statistical model using observations that issues forecasts for March (as in https://github.com/achevuturi/PEACFLOW_Manaus-flood-forecasting/tree/master/Using_Observations) which is implemented here with input from combination of observations and seasonal forecasts.

**Citation:**
Users who apply the code resulting in presentations/publications are kindly asked to cite the publication below:\
*Chevuturi A, Klingaman NP, Woolnough SJ, Rudorff CM, Coelho CAS, Schongart J (2021) Extending forecast lead time for annual maximum water level at Manaus using seasonal forecasts. Climate Resilience and Sustainability, in prep.*
