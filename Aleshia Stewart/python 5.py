# Assignment1.py
# Aleshia Stewart


class Person :
    def __init__ (self,name=' ', email=' '):
        self.firstname = name
        self.lastname = name
        self.email = email

    def ask_for_data (self) :
        print("enter the name and the email address")

        self.firstname = input ("input first name")
        if self.firstname =="" :
            return
        self.lastname= input ("input last name")
        self.email= input ("input email address")

    def savedata (self):
        eline = '"'+self.firstname+'", "'+self.lastname+'", "'+self.email+"\n"
        e=open ("E:/namesandaddress.csv",'a')
        e.writelines(eline)
        e.close ()

while False: #True:
    entry=Person ()
    entry.ask_for_data ()
    if entry.firstname =="" :
        break
    entry.savedata ()
    

##"""
e=open ("E:/namesandaddress.csv",'r')
x=e.readlines ()
##>>>  x
for line in x:
    y=line.split(',')
    fname=y[0][1:-1]
    lastname=y[1][1:-1]
    email=y[2][1:-1]
    # print the form letter:
    print ('dear' + fname+' '+lastname+ ' is this your correct email address? ' + email)
    
##"""

