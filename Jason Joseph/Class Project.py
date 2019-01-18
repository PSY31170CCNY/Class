#What is the need of the program that I am writing for this data?
#Comparing the number of HIV diagnosis in different racial group in NYC
#Comparing the number of HIV diagnosis in different neighborhoods in NYC

import csv
file="C:/Users/jjoseph005/Desktop/HIV_AIDS_Diagnoses_by_Neighborhood__Age_Group__and_Race_Ethnicity.csv"

        
year=0 # year the data was taken
hood=1 # location of the data collection 
race=2 # racial makeup 
age=3 # age of the cohort
totalhiv=4 # total cases of HIV
hiv100=5     # total cases of HIV per 100,000
cohiv=6      # Number of cases with concurrent HIV and AIDS diagnoses

class HIVDATA:
     def __init__(self,year='', hood='', race='',age = '',\
                 totalhiv='',hiv100='',cohiv=''):

         self.year= year
         self.hood= hood
         self.race= race
         self.age = age
         self.totalhiv = totalhiv
         self.hiv100= hiv100
         self.cohiv = cohiv

with open(file,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    racedict={}
    for row in csvreader:
        if not row[race] in racedict.keys():
            racedict[row[race]]=[]
        racedict[row[race]].append(row) # {"year":row[year],"hood":row[hood],"age":row[age],"totalhiv":row[totalhiv],"hiv100":row[hiv100],"cohiv":row[cohiv]}
        
    
    #row in csvreader:
        #print(",".join(row))
