#classproject.py
#this is an analysis of Housing Litigations 
#download from:https://data.cityofnewyork.us/Housing-Development/Housing-Litigations/59kj-x8nc
import csv
litid = 0 #Litigationid has a unique id
bldg = 1 #Building id
borough =2  #Each borough with code numbers
bcodes = {'1':'Manhattan','2':'Bronx','3':'Brooklyn','4':'Queens',\
          '5':'StatenIsland'} # to convert the codes into text
#Skip HouseNumber
street=3 #street name with GIS street code
zipcode=4 #Zipcode of each building
block=5 # DoF identifier of what lot the building is on
casetype=6#Type of building violations
casedate=7# When the case was open
nta=8 #where the court case occurred
##
class Housing:
    def __init__(self,buildingid='', street='', zipcode='',borough='', block='',\
                 litigationid='', casetype='', casedate= '', nta=''):

        
           self.buildingid = buildingid
           self.street = street
           self.zipcode = zipcode
           self.borough = borough
           self.block = block
           self.litigationid = litigationid
           self.casetype = casetype
           self.casedate = casedate
           self.nta = nta
           
## This is a comparison between the number of violations filed by Tenants and HPD in Broolyn
Tenant = {}# cases issued by tenants against their landlords
HPD = {}# cases issued by HPD against landlords for outstanding building violations 
datafile = '/Users/okolawo000/Desktop/Housing_Litigations.csv'

with open(datafile, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ',', quotechar='|')
    
    for row in csvreader:
        
        
        lc = row[casetype].lower() #converts casetype into lower case.
        if not(('tenant' in lc) or ('comprehensive' in lc)):
            continue
        #Create a Housing object
        h = Housing(row[litid],row[casetype],row[casedate],' '.join([row[bldg],row[street]]),\
                    row[borough],row[nta])
        
        if lc in 'tenant': #remember lc keeps casetype value in lowercase
            Tenant[row[litid]]=h
        else:
            HPD[row[litid]]=h
Tencount=len(Tenant)
Hpdcount=len(HPD)

tenkeys = Tenant.keys()
hpdkeys = HPD.keys()

def countup(housdict, borough=2):
    hlist=housdict.keys()
    boroughdict={}
    for h in hlist:
        row=housdict[h]
        borough=row.borough
        if borough in boroughdict:
            boroughdict[borough] +=1
        else:
            print(borough,str(row.litid))
        return housdict
tentcase = countup(Tenant,borough)
HPDcase = countup( HPD,borough)
  



        
        
        
