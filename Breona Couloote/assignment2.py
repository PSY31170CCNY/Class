#assignment
class Person:
    def __init__(self,firstname='',lastname='',email=''):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def hello(self):
        print("hi",self.name)
        
    def askdata(self):
        self.firstname = input("enter first name")
        if self.firstname=='':
            return
        self.lastname = input("enter last name")
        self.email = input ("enter email")
        

people=[]

drive='C:/Users/bcouloo000/Desktop/'

e=open(drive+'emaillist.csv','r')

emails=e.readlines() 

e.close()


for p in e:
    print('text string of this line:',p)
    data = p.split(',')
    print("Dear "+p.firstname+ " "+p.lastname+ "Is this your correct email address?"+ " "+p.email

print("\nThe raw peopledict is:\n",peopledict)
print("---- now displayed by key-value pairs:")
for p in peopledict.keys():
    print("lookup key:",p,"value:",peopledict[p][0:-1])
print('===\n')
n=''
while n == '':
    n=input("Go ahead, enter a name to look up their data (or q to quit):")
    if n in'Qq':
        break
    try:
        print("Error: ",n,"not found in peopledict. Try again or q to quit.")
    except:
        print("Error: ",n,"not found in peopledict. Try again or q to quit.")
        n=''

def getpersondata(data ={'lastname':'','firstname':'','email':''}):
    fields=['lastname','firstname','email']
    for field in fields:
        if len(data[field]>0):
            x=input("change "+field+ " from "+data[field]+"(Y/N)")
            if x not in 'Yy':
                continue
        data[field]=input("enter the person's "+field )
    return data

while True:
    pname = input('enter the name of the person to find:')
pdata = persons[pname]

try:
    pdata = persons[pname]
except:
    addnew = input(pname+' not found. Add as new (Y/N)?')
    if addnew in 'Yy':
        persons[pname] = [pname]
    else:
        contnue
data=getpersondata(pdata)
