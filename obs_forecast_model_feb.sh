#!/bin/bash
# This script will give you the forecast for the year requested (2005 onwards)

tput setaf 1 #red
echo "Forecast model for maximum water level of Negro River at Manaus (lead time FEBRUARY)"

echo "Please enter the year for which the forecast is requred (YYYY, 4 digits 2005 onwards), followed by [ENTER]:"
tput sgr0 #black

read year

tput setaf 1 #red
echo "Downloading CHIRPS data for NDJ"
tput sgr0 #black

wget https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p05/by_month/chirps-v2.0.$((year-1)).11.days_p05.nc
wget https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p05/by_month/chirps-v2.0.$((year-1)).12.days_p05.nc
wget https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p05/by_month/chirps-v2.0.$year.01.days_p05.nc

tput setaf 1 #red
echo "Merging CHIRPS data for NDJ and converting to monthly means"
tput sgr0 #black

cdo mergetime chirps-v2.0.????.??.days_p05.nc chirps-v2.0.$((year-1))-$year.ndj.days_p05.nc

cdo monmean chirps-v2.0.$((year-1))-$year.ndj.days_p05.nc chirps-v2.0.$((year-1))-$year.ndj.mons_p05.nc

rm -f chirps-v2.0.*.days_p05.nc  

tput setaf 1 #red
echo "Downloading AMO data"
tput sgr0 #black
wget https://psl.noaa.gov/data/correlation/amon.us.long.data 
head -n -4 amon.us.long.data > amo.txt
rm -f amon.us.long.data

tput setaf 1 #red
echo "Running the forecasting model for $year"
tput sgr0 #black

python3.7 -W ignore obs_forecast_model_feb.py $year

tput setaf 1 #red
echo "Deleting dowloaded data"
rm -f amo.txt chirps-v2.0.*.mons_p05.nc
tput sgr0 #black
