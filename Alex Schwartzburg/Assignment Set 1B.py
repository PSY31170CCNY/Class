#Assignment Set 1B

DatabaseExtension = "C:/Users/aschwar002/Desktop/01.15.2019/"
DatabaseFilename = "email list02.csv"

Extension = "C:/Users/aschwar002/Desktop/01.15.2019/"#input("Where would you like to create your file?\n###Enter the file path.")
Filename = "FormLetter.txt" #input("What would you like to call this file?\n###Enter the filename.")
##Contents = input("What would you like the file to say?")
File = Extension + Filename

###Grabbing their name
##name = input("Who are you contacting?\n###Enter their name.")
##
###Grabbing their email
##email = input("What is their email?\n###Enter their email.")

e = open(DatabaseExtension+DatabaseFilename,'r')
namelist = e.readlines()
fieldnames = ["firstname","lastname","email"]
e.close()
mergeList=[]
for name in namelist:
    fields = name.split(',')
    print(fields)
    n=0
    names = {}
    for field in fields:
        item = field
        names[fieldnames[n]] = item
        n=n+1
    mergeList.append(names)
print("Printnames")
print(names)

f = open(File,'a')
for x in mergeList:
    var01 = "Dear "+x["firstname"]+" "+x["lastname"]+',Is this your correct email address? '+x["email"]+"\n"
    print(var01)
    f.writelines(var01)
f.close()




