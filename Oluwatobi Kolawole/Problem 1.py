drive='/Users/okolawo000/Desktop/'
e=open(drive+'contactlist.csv','w')
Rename = True
while Rename:
    Info = input("Would you like to insert a new person? Y/N")
  
    while Info in "Yy/YES/yes":
        A= input("What is your first name?")
        B = input("What is your last name?")
        C= input("Enter your email address.")
        
        Data = str('"'+ A +'",'+'"'+ B +'",'+ C +'\n')
        
        
        e.writelines(Data)
        e.close()
        continue
    print("Try again. Please try again")               
    
