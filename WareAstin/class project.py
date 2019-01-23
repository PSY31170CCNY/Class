import csv 
file = " insert the location of the csv file here if any, otherwise don't include this line"

hosp = 0
quest = 1
ans = 2 
ansp = 3 

class patient
def __init__(self,hosp='', quest='', ans='', ansp =''):
self.hosp=hosp
self.quest=quest
self.ans=ans
self.ansp=ansp

hospdict={}

with open(file,newline='') as csvfile:
csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
for row in csvreader:
if not row[hosp] in hospdict.keys():
hospdict[row[hosp]]=[]
hospdict[row[hosp]].append(row)

or 

with open(file,newline='') as csvfile:
csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
for row in csvreader:
c = PATIENT(row[hosp],row[quest],' '.join([row[ans],row[ansp]])

Sent from my iPhone
