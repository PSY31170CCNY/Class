extension='/Users/alugo0_0/Desktop/Assignment 1 .py (3.7.2)'
filename="personaldata.csv"

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


