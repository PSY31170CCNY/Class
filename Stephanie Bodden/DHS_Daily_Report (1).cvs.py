# classproject.py
# This is an analysis for the Department of Homeless (DHS) within NYC
# Found in file:
# DHS_Daily_Report
# Downloaded from https://data.cityofnewyork.us/Social-Services/DHS-Daily-Report/k46n-sa2m on 1/18/2019

import csv
with open ('/Users/sbodden000/Downloads/DHS_Daily_Report.csv') as csvfile:
    r = csv.reader(csvfile)
    for row in r:
        print (row)

#Analysis the following from the dataset 'Total Adults in Shelter', 'Total Children in Shelter', 'Single Adult Men in Shelter', 'Single Adult Women in Shelter'.
#Looking at the data following 1/1/2014 to 12/31/2018 in yearly incorements (Over a 5 year span)
#Data from 1/1/2014 to 12/31/2014, Data from 1/1/2015 to 12/31/2015, Data from 1/1/2016 to 12/31/2016, Data from 1/1/2017 to 12/31/2017, Data from 1/1/2018 to 12/31/2018.


