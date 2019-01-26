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
#['35838', '107073', '2', '3145', 'ROCHAMBEAU AVENUE', '10467', '3335', '12', 'Tenant Action', '7/3/2006 0:00', 'CLOSED', 'NO', '', '', '', 'OSCAR ROJAS', '40.874428', '-73.880371', '7', '11', '419', '2017986', '2033350012', 'Norwood']
street=4 #street name with GIS street code
zipcode=5 #Zipcode of each building
block=6 # DoF identifier of what lot the building is on
casetype=8#Type of building violations
casedate=9# When the case was open


##
class Housing:
    def __init__(self,buildingid='', address='', zipcode='',borough='', block='',\
                 litigationid='', casetype='', casedate= '', ):

        
           self.buildingid = buildingid
           self.address = address
           self.zipcode = zipcode
           self.borough = borough
           self.block = block
           self.litigationid = litigationid
           self.casetype = casetype
           self.casedate = casedate
          
           
## This is a comparison between the number of violations filed by Tenants and HPD in each of the five boroughs
Tenant = [[],[],[],[],[],[]]# cases issued by tenants against their landlords
HPD = [[],[],[],[],[],[]]# cases issued by HPD against landlords for outstanding building violations 
datafile = '/Users/okolawo000/Desktop/Housing_Litigations.csv'
houses=[[],[],[],[],[],[]]

with open(datafile, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ',', quotechar='|')
    print(datafile ,'is open')
    for row in csvreader:
        
        
        lc = row[casetype].lower() #converts casetype into lower case.
        if not(('tenant' in lc) or ('comprehensive' in lc)):
            continue
        if int(row[borough]) is not [1,2,3,4,5]:
           row[borough]= 6
        #Create a Housing object
        h = Housing(litigationid=row[litid],casetype=row[casetype],casedate=row[casedate],address=' '.join([row[bldg],row[street]]),\
                    borough=int(row[borough]))
        print(h.borough)

        houses[h.borough-1].append(h)
        if lc in 'tenant': #remember lc keeps casetype value in lowercase
            Tenant[h.borough-1].append(h)
        else:
            HPD[h.borough-1].append(h)
Tencount=len(Tenant)

for b in range(len(Tenant)):

    tottencount += len(Tenant[b])
Hpdcount=len(HPD)
for h in range(len(HPD)):
    totHpdcount += len(HPD[h])
print(tottencount)

    



        
        
        
