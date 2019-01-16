class Person:
    def __init__(self,firstname='', lastname='',email=''):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

e=open("names.txt","r")
names=e.readlines()
for line in names:
    #Decide if it's blank, name, or email line.
    #If the length of line is zero than it's blank. (Skip it)(Continues loop)
    if len (line)== 0:
        continue
    x=line.split()
    if len (x)==2:
        firstname=x[0]
        lastname=x[1]
        p=Person(firstname, lastname, email='')
    if len (x)==1
        p.email=x
        email=x[1]
        p=Person(firstname, lastname, email)
        
        
    
