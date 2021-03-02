
**Flood forecasting for Negro River at Manaus using seasonal forecasts for February lead-time**

**Description:**
This module contains models for forecasting maximum water level for Negro River at Manaus for any year from 2017 onwards using combination of observations and ECMWF seasonal forecasts as input. The required input data files are available in the parent directory (https://github.com/achevuturi/PEACFLOW_Manaus-flood-forecasting/tree/master/Using_Seasonal-Forecasts). This sub-folder has one model that provides forecasts at Februrary lead-time for each year. 

**Modules:**

**Execution:** The model works by running the shell script for the forecast using the example command **./feb_forecast.sh** OR **source feb_forecast.sh**. After this command, the user needs to provide the year for which the forecast is required (2017 onwards) when prompted by the script to complete the run.

**Output:**
The esemble mean forecast of the maximum water level of Negro River at Manaus (in meters) is given in the command line, and the ensemble forecast is saved as an output .csv file. All the downloaded data is then deleted.

**Acknowedgement:** Please include the following form of acknowledgement in any presentations/publications that use any of the code stored in this repository.\
*"The development of PEACFLOW_Manaus-flood-forecasting repository Using_Seasonal-Forecasts module on GitHub (https://github.com/achevuturi/PEACFLOW_Manaus-flood-forecasting/tree/master/Using_Seasonal-Forecasts) was supported by the Newton Fund through the Met Office Climate Science for Service Partnership Brazil (CSSP Brazil) and was developed at University of Reading."*

**Citation:**
Users who apply the code resulting in presentations/publications are kindly asked to cite the publication below:\
*Chevuturi A, Woolnough SJ, Klingaman NP, Rudorff CM, Coelho CAS, Schongart J (2021) Extending forecast lead time for annual maximum water level at Manaus using seasonal forecasts. Climate Resilience and Sustainability, in prep.*
