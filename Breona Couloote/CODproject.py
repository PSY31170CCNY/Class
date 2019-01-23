#classprojectCOD
#the files are looking at New York City Leading Cause of Death
#my project is comparing males andvfemales leading cause of death 
import csv
#link:
#https://data.cityofnewyork.us/Health/New-York-City-Leading-Causes-of-Death/jb7j-dtam 
uid=0 #unique id 
year = 1 #year of death
cause = 2 #cause of death
sex = 3
race = 4
death = 5 #number of deaths
dr = 6 #death rate
age = 7 #age rate
#making a class to hold the datawhat is in the excel file
class COD:
    def __init__(self,uniqueid='',year='', cause='', sex='', race='',death='',\
                 dr='',age=''):
        self.uniqueid=uniqueid
        self.year=year
        self.cause=cause
        self.sex=sex
        self.race=race
        self.death=death
        self.dr=dr
        self.age=age

Female= {}
Male= {}
datafile = "New_York_City_Leading_Causes_of_Death.csv"

with open(datafile, newline='') as csvfile:
    datareader = csv.reader(csvfile,delimiter = ',', quotechar='|')
    for row in datareader:
        lc = row[sex].lower()
        if not(('female' in lc) or ('male' in lc)):
            continue

    c = COD(row[year],row[uid],row[cause],' '.join([row[sex],row[race],row[death],row[dr],row[age]])
if lc in 'sex': #im getting an invalid syntax error. I've tried everything to fix not sure why the error is happening
            Female[row[uid]]=c
else:
            Male[row[uid]]=c

Femcount=len(Female)
Malcount=len(Male)

femkeys = female.keys()
malkeys = male.keys()

def causecount(coddict,cause=2):
    clist=coddict.keys()
    causedict={}
    for c in clist:
        row=coddist[c]
        cause=row.cause
        if cause in causedict:
            causedict[cause] +=1
        else:
            print(cause,str(row.uniqueid))
            causedict[cause]=1
    return gradedict
femcause = causecount(Female,cause)
malcause = causecount(Male,cause)
for d in 'ABCZ':
    print('female cause ',d ,femcause[d])
    print('male cause ',d ,malcause[d])
    

                
