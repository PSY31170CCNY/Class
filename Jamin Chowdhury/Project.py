import csv
Destination = "C:/Users/Jamin/Desktop/project/"
Filename = "Drinking_Fountains.csv"
File = Destination + Filename

num = 0  #Property Number
name = 1  #Site Name
boro = 2  #Borough
drink = 3  #Fountains

with open(File, newline='') as csvfile:
    Filereader = csv.reader(csvfile,delimiter = ',', quotechar='|')
    park = {}
    for row in Filereader:
        PropertyNumber[row[1]]= Parks(row[0],row[1],row[2],row[3])
        PropertyNumber[row[0]]={'SitName':row[1],'Borough':row[2],'Fountains':row[3]}
        
class Parks:
    def __init__ (self, num='', name='', boro='',drink =''):
        self.num = PropertyNumber
        self.name = SiteName
        self.boro = Borough
        self.drink = Fountains
        
FountainList=restdict.keys()
    ParkListdict={}
    for P in FountainList:
        row=restdict[p] 
        ParkList=row.ParkList
        if ParkList in ParkListdict:
            ParkListdict[ParkList] += 1
        else:
            print(ParkList,str(row.ParkNumber))
            ParkListdict[ParkList]=1 
    return ParkListdict


   
