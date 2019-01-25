#Locate and Generate
Destination = "C:/Users/Jamin/Desktop/PythAss1/"
Filename = "Email List.csv"
File = Destination + Filename
#-----------------------------------------------------

#Ask the Task
begin = input("Do you want to generate the form letter using the 'Email List'? Y/N")
while begin in "Yy":
#Referring to whatever relevant Email List.csv was created prior.
    v1 = input("To do this we must Open the Email List. Are you okay with that? Y/N")
    while v1 == "Yy": 
        v1 = input("Okay. Press ‘Enter’ to continue!")
    if v1 == '':
#-------------------------------------------------------

        Email = open(Destination+Filename,'r')
        FormList = Email.readlines()
        Email.close()
#Opens aforementioned CSV.
#-------------------------------------------------------

    mergeList = []

    for things in FormList:
        listparts = things.split(',')
        mergeList.append(listparts)
#Using FirstName+LastName+EmailAddress,it creates a list.
            
    print(FormList)
#-------------------------------------------------------

Destination2 = "C:/Users/Jamin/Desktop/PythAss1/"
Filename2 = "Form Letter.txt"
FormFile = Destination2 + Filename2

#Printing the Form Letter's text file into the same folder of CSV.
#--------------------------------------------------------

f = open(FormFile,'a')
#Opens the Text File in which the Form List will be generated.
for formparts in mergeList:
        v3 = "Dear "+formparts[0]+" "+formparts[1]+',is this your correct email address? '+formparts[2]+"\n"
        print(v3)
        f.writelines(v3)
f.close()
#Converts the FirstName+LastName+EmailAddress list into a question that looks like:
#"Dear FirstName" "LastName" , is this your correct email address? "EmailAddress."? "
#--------------------------------------------------------------







