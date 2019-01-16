#Locate and Create
#----------------------------------------

Destination = "C:/Users/Jamin/Desktop/PythAss1/"
Filename = "Email List.csv"
File = Destination + Filename

#----------------------------------------


#Header
#----------------------------------------
z1 = ('First Name')
z2 = ('Last Name')
z3 = ('Email Address')
v0 = str('"'+z1+'",'+'"'+z2+'",'+z3+'\n')

f = open(File,"a") #append
f.writelines(v0)
#----------------------------------------


#Program
#----------------------------------------
List = True
while List:
    v1 = input("Would you like to contribute to the Email List? Y/N")
    if v1 in 'Nono':
        print("It would be really helpful if you did!") 
    while v1 in "Yesyes":
        v2 = input("Person's last name.")
        if v2 == "":
            break
        v3 = input("Person's first name.")
        if v3 == "":
            break
        v4 = input("Person's email address.")
        if v4 == "":
            break
        v5 = str('"'+v3+'",'+'"'+v2+'",'+v4+'\n')
        # First Name, Last Name, Email Address formatting
        f = open(File,"a") #append
        f.writelines(v5)
        f.close()
        continue
#------------------------------------------
