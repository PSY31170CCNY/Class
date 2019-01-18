import csv
file="C:/Users/jjoseph005/Desktop/HIV_AIDS_Diagnoses_by_Neighborhood__Age_Group__and_Race_Ethnicity.csv"
with open(file,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in csvreader:
        print(",".join(row))
        
    
class HIV:
     def __init__(self,year='', hood='', race='',age = '',\
                 totalhiv='',hiv100='',cohiv=''):

         self.year= year
         self.hood= hood
         self.race= race
         self.age = age
         self.totalhiv = totalhiv
         self.hiv100= hiv100
         self.cohiv = cohiv
