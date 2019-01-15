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

while True:
    entry=Person ()
    entry.ask_for_data ()
    if entry.firstname =="" :
        break
    entry.savedata ()
    




