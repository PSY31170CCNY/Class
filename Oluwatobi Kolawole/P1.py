Drive = "C:/Users/okolawo000/Desktop/"
Filename = "contactlist.csv"
e=open(Drive+Filename,'w')
Rename = True
while Rename:
    Info = input("Would you like to insert a new person? Y/N")
    if Info =="N":
        break
    while Info in "Yy/YES/yes":
        A= input("What is your first name?")
        if A =="":
            break
        B = input("What is your last name?")
        if B =="":
            break
        C= input("Enter your email address.")
        if C =="":
            break

Data = str('"'+ A +'",'+'"'+ B +'",'+ C +'\n')

e.open(Drive+Filename)
e.writelines(Data)
e.close()

print("Try again. Please try again")       
