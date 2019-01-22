#classprojectCOD
import csv

uid=0
year = 1
cause = 2
sex = 3
race = 4
death = 5
dr = 6 #death rate
age = 7

class COD:
    def __init__(self,uid='',year='', cause='', sex='', race='',death='',dr='',age=''):
        self.uniqueid=uniqueid
        self.year=year
        self.cause=cause
        self.sex=sex
        self.race=race
        self.death=death
        self.dr=dr
        self.age=age

hispanic = {}
black = {}
datafile = "New_York_City_Leading_Causes_of_Death.csv"

with open(datafile,newline='') as csvfile:
    datareader = csv.reader(csvfile,delimiter = ',', quotechar='|')
    for row in datareader:
        lc = row[race].lower()
        if not(('hispanic' in lc) or ('black' in lc)):
            continue

    c = COD(row[year],row[uid],row[cause],' '.join([row[sex],row[race],row[death],row[dr],row[age]])

    if lc in 'hispanic':
        hispanic[row[uid]]=c
    else:
         black[row[uid]]=c

hiscount = len(hispanic)
blackcount = len(black)

hiskeys = hispanic.keys()
blackkeys = black.keys()

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

Hiscause = causecount(hispanic,cause)
Blackcause = causecount(black,cause)
for s in 'ABCZ':
    print('black cause ',s ,Hiscause[s])
    print('hispanic cause ',s ,Blackcause[s])
    

                
