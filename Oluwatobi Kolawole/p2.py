extension='/Users/okolawo000/Desktop/P1 .py (3.4.3)'
filename="personalinfo.csv"

f=open(extension+filename,"w")
f.close()


Rename=True 

while Rename:

    firstname = input("What is your first name:")
    if firstname=="":
        break 
    lastname= input("What is your last name:")
    email= input("Enter your email name:")
    data=(firstname,",",lastname,",",email,'\n')

    ff=open (extension+filename,"a")
    ff.writelines(data)
    ff.close()
    
    
    print(data)

print("TRY AGAIN")
##
ff=open(extension+filename,"r")
x=ff.readlines(data)
for line in x:
    y=line.split(',')
    print( "Dear" +firstname+" "+lastname+" is this your correct email address?"+email)
ff.writelines(y)
ff.close()
