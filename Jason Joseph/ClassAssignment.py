#What is the need of the program that I am writing for this data?
#Comparing the number of SAT scores in different schools in NYC
#Which school had higher math scores?


#SAT.csv
import csv
file="C:/Users/jjoseph005/Desktop/SAT.csv"

        
DBN=1 # year the data was taken
school=2 # school location
notest=3 # number of test takers
reading=4 # reading score
math=5 # math score
writing=6     # writing score



#dictionary creation with the school as the key for the subsequent scores

with open("SAT.csv",newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    school={}#dictionary to access SAT data by the school 
    for row in csvreader:
        school[row[1]]={'notest':row[2],'reading':row[3],'math':row[4],'writing':row[5]} #defining the key as the school name and the different SAT scores
        
  
#object creation  
class SATDATA:
     def __init__(self,DBN='', school='', notest='',reading = '',\
                 math='',writing=''):

         self.DBN= DBN
         self.school= school
         self.notest= notest
         self.reading = reading
         self.math = math
         self.writing= writing
#CENTRAL PARK EAST HIGH SCHOOL
        #HIGH SCHOOL OF GRAPHIC COMMUNICATION ARTS
#interface for the user to call the data up and compare values
         
start=input("Would you like to compare the scores of different schools? (Y/N)")

if start == "Y":
    x=input("Cool which score would you like to look at? Writing/Reading/Math")
    if x == "Math":
        math1=input("What is the first school you would like to choose?")
        print(school[math1]["math"])
        math2=input("What is the second school you would like to choose?")
        print(school[math2]["math"])
    elif x == "Writing":
        write1=input("What is the first school you would like to choose?")
        print(school[write1]["writing"])
        write2=input("What is the second school you would like to choose?")
        print(school[write1]["writing"])
    elif x == "Reading":
        read1=input("What is the first school you would like to choose?")
        print(school[read1]["reading"])
        read2=input("What is the second school you would like to choose?")
        print(school[read1]["reading"])
    
elif start== "N":
    print("Next time then")

tallyup=input("Would you like to know the averaget total SAT score for each school? (Y/N)")
if tallyup == "Y":
    totalavg=(input("What school average total would you like to compute?"))
    intmath=int(school[totalavg]["math"])
    intwrite=int(school[totalavg]["writing"])
    intread=int(school[totalavg]["reading"])
    inttotal=int(intmath+intwrite+intread)
    print(school[totalavg]["math"], school[totalavg]["writing"], school[totalavg]["reading"],"=",inttotal)

elif tallyup == "N":
    print("Alrighty!")
              
    

       
