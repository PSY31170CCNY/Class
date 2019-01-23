Assignments:

1. Write a program that creates a list of names and email addresses
    • loop to let a user enter a name and an email address  until they enter a blank line
        ◦ enter last name
        ◦ enter first name
        ◦ enter email address
        ◦ Save each entry at the end of a csv file as “firstname”, “lastname”, “email”
2. Write a program that lets the use enter a file name containing text for a form letter and generates the form letter using the email list
    • enter file name
    • open file and read in the text
    • enter the name of the email file from #1 and open it
    • loop through the email entries 
        ◦ create a filled out form letter  with the first and last name and email address
        ◦ e.g.: Dear Bob Smith, Is this your correct email address?  bobs@gmail.com
        ◦ print the form letter
        
f=open(extension+filename,"w")
f.close()


morenames=True 

while morenames:

    lastname = input("Enter your last name:")
    if lastname=="":
        break 
    firstname= input("Enter your first name:")
    email= input("Enter your email name:")
    dataentry=(lastname,",",firstname,",",email,'\n')

    ff=open (extension+filename,"a")
    ff.writelines(dataentry)
    ff.close()
    
    
    print(dataentry)

print("No More Data Entry")


class Person:
    def __init__(self,name='',email=''):
        self.name = name
        self.email = email

    def hello(self):
        print("Hi there! My name is ",self.name)

# test the class:
Sally = Person('Sally','1 Any Way','123-4567','sally@gmail')




Stephanie = Person(name='Bodden,Stephanie',email='sbodden00@citymail.cuny.edu')

"Abdullah" "Abdull" "Abdullabdullah96@gmail.com"
"Stewart" "Aleshia" "aschwartzburg@gmail.com"
"Lugo" "Ariell" "alugo001@citymail.cuny.edu"
"Couloote" "Breona" "bcouloote@gmail.com"
"Coumswang" "Daniel" "daniel.coumswang@gmail.com"


e=open("names.txt","r")
names=e.readlines()


Abdull Abdullah
Abdullabdullah96@gmail.com

Aleshia Stewart 
astewar005@citymail.cuny.edu

Alex Schwartzburg
aschwartzburg@gmail.com

Ariell Lugo
alugo001@citymail.cuny.edu

Breona Couloote 
bcouloote@gmail.com

Daniel Coumswang
daniel.coumswang@gmail.com

Jamin Chowdhury
jchowdh000@citymail.cuny.edu

Jason Joseph
jajosepho3@gmail.com

Justin Pearce
justinpearce231@gmail.com

Oluwatobi Kolawole
oluwatobi.kolawole8613@gmail.com

Ramon Brito 
ramonbrito89@gmail.com

Ware Astin
wastin000@citymail.cuny.edu





e=open("names.txt","r")
names=e.readlines()


nametext="firstname lastname"
nameparts=nametext.split()
[firstname,lastname]
cvsv='"'+firstname'",'+'"'+lastname+'"\n'



linetype="name"
if linetype equals name

