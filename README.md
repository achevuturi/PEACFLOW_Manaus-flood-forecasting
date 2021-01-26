**Manaus_flood_forecasting**

**Author:**
Amulya Chevuturi, National Centre for Atmospheric Science, Department of Meteorology, University of Reading, Reading, UK

**Project and Funding:**
Forecast model from the Predicting the Evolution of the Amazon Catchment to Forecast the Level Of Water (PEACFLOW) project. PEACFLOW project is funded by Newton Fund through the Climate Science for Service Partnership (CSSP) Brazil project at UK Met Office.

**Description:**
The software contained in this repository forecasts maximum water level for Negro River at Manaus for any year from 2005 onwards. This repository has a shell script (.sh) which downloads the requred CHIRPS rainfall estimate and executes the flood forecasting model (.py and .pkl) to give the flood forecast for the year requested. There are three different forecast models hosted within the repository, which forecast maximum water level at Manaus at three different lead times: March (obs_forecast_model_mar.sh), February (obs_forecast_model_feb.sh) and January (obs_forecast_model_jan.sh). For any current year, the forecast models only work after the middle of the month of the forecast, due to the lag in the CHIRPS rainfall uploads.

**Requirements:**
To run the models hosted in this repository needs Python (version3.7; https://www.python.org/downloads/source/) and CDO (version1.9; https://code.mpimet.mpg.de/projects/cdo/). The package also requires installation of the the Python packages: Cf-Python (https://ncas-cms.github.io/cf-python/); Numpy (http://www.numpy.org) and Pandas (https://pandas.pydata.org/)

**Modules:**
Below th

**Execution:**
The model works by running the shell scripts of the month which needs the forecast using the example command below: 
./obs_forecast_model_mar.sh
After this command, the user needs to provide the year for which the forecast is required (2005 onwards) when prompted by the script to complete the run. 
1. For the **forecasts in March** use **./obs_forecast_model_mar.sh**
2. For the **forecasts in February** use **./obs_forecast_model_feb.sh**
3. For the **forecasts in January** use **./obs_forecast_model_jan.sh**

**Output:**
The forecast of the maximum water level of Negro River at Manaus (in meters) is given in the command line. All the downloaded data (CHIRPS rainfall and AMO index text file) is deleted.

**Citation:**
Users who apply the software resulting in presentations or papers are kindly asked to cite:
Chevuturi et al.........


