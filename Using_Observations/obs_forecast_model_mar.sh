#!/bin/bash
# This script will give you the forecast for the year requested (2005 onwards) for March lead time

tput setaf 1 #red
echo "Forecast model for maximum water level of Negro River at Manaus (lead time MARCH)"
echo "Please enter the year for which the forecast is requred (YYYY, 4 digits 2005 onwards), followed by [ENTER]:"
tput sgr0 #black
read year

tput setaf 1 #red
echo "Downloading CHIRPS data for NDJF"
tput sgr0 #black
wget https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p05/by_month/chirps-v2.0.$((year-1)).11.days_p05.nc
wget https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p05/by_month/chirps-v2.0.$((year-1)).12.days_p05.nc
wget https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p05/by_month/chirps-v2.0.$year.01.days_p05.nc
wget https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p05/by_month/chirps-v2.0.$year.02.days_p05.nc

tput setaf 1 #red
echo "Merging CHIRPS data for NDJF and converting to monthly means"
tput sgr0 #black
cdo mergetime chirps-v2.0.????.??.days_p05.nc chirps-v2.0.$((year-1))-$year.ndjf.days_p05.nc
cdo monmean chirps-v2.0.$((year-1))-$year.ndjf.days_p05.nc chirps-v2.0.$((year-1))-$year.ndjf.mons_p05.nc
rm -f chirps-v2.0.*.days_p05.nc  

tput setaf 1 #red
echo "Downloading previous year's minimum value"
tput sgr0 #black
wget https://www.portodemanaus.com.br/?pagina=niveis-maximo-minimo-do-rio-negro -O webpage.txt
var=`grep -n ">$((year-1))</td>" webpage.txt | cut -f1 -d":"`
awk "NR==$((var+3))" webpage.txt | tail -c 12 | cut -c1-5 > prev_min.txt
rm -f webpage.txt

tput setaf 1 #red
echo "Downloading AMO data"
tput sgr0 #black
wget https://psl.noaa.gov/data/correlation/amon.us.long.data 
head -n -4 amon.us.long.data > amo.txt
rm -f amon.us.long.data

tput setaf 1 #red
echo "Running the forecasting model for $year"
tput sgr0 #black
python3.7 -W ignore obs_forecast_model_mar.py $year

tput setaf 1 #red
echo "Deleting dowloaded data"
rm -f prev_min.txt amo.txt chirps-v2.0.*.mons_p05.nc
tput sgr0 #black
