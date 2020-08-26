#!/bin/bash
# This script will give you the forecast for the year requested (2005 onwards)


tput setaf 1 #red
echo "Please enter the year for which the forecast is requred (YYYY, 4 digits 2005 onwards), followed by [ENTER]:"
tput sgr0 #black

read year

tput setaf 1 #red
echo "Downloading CHIRPS data for NDJF"
tput sgr0 #black
#Downloading monthly data from https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p05/by_month/

wget https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p05/by_month/chirps-v2.0.$((year-1)).11.days_p05.nc
wget https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p05/by_month/chirps-v2.0.$((year-1)).12.days_p05.nc
wget https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p05/by_month/chirps-v2.0.$year.01.days_p05.nc
wget https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p05/by_month/chirps-v2.0.$year.02.days_p05.nc

tput setaf 1 #red
echo "Merging CHIRPS data for NDJF and converting to monthly means"
tput sgr0 #black

cdo mergetime chirps-v2.0.????.??.days_p05.nc  chirps-v2.0.$((year-1))-$year.ndjf.days_p05.nc
rm -f chirps-v2.0.????.??.days_p05.nc  
cdo monmean chirps-v2.0.$((year-1))-$year.ndjf.days_p05.nc chirps-v2.0.$((year-1))-$year.ndjf.mons_p05.nc
rm -f chirps-v2.0.????.??.days_p05.nc  chirps-v2.0.$((year-1))-$year.ndjf.days_p05.nc

tput setaf 1 #red
echo "Running the forecasting model for $year"
tput sgr0 #black

python3.7 -W ignore forecast_model.py $year

#rm -f chirps-v2.0.$((year-1))-$year.ndjf.mons_p05.nc
