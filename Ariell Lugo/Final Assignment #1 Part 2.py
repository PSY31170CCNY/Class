#Final Assignment #1 Part 2

#Variable assignments
##First Choice
var1 = input("Would you like to create a new file or use the default? \n1 - Use Default.\n2 - Create new file.")
#if var1 = 1, use default.
while var1 == "":
    var1 = input("Would you like to create a new file or use the default? \n1 - Use Default.\n2 - Create new file.")
else:
    if var1 == '1':
        Extension = "C:/Users/alugo0_0/Desktop/"
        Filename = "A#1part2.txt"
    elif var1 == '2':
        Extension = input("Where would you like to create your file?\n###Enter the file path.")
        Filename = input("What would you like to call this file?\n###Enter the filename.")

##2nd Choice - which database do you want to use?
var2 = input("Would you like to use the default database or call a new one? \n1 - Use Default.\n2 - Create new file.")
###if var2 = 1, use default.
while var2 == "":
    var2 = input("Would you like to use the default database or call a new one? \n1 - Use Default.\n2 - Create new file.")
else:
    if var2 == '1':
        DatabaseExtension = "C:/Users/alugo0_0/Desktop/"
        DatabaseFilename = "email_list.csv"
    elif var2 == '2':
        DatabaseExtension = input("Where is the database?\n###Enter a file path.")
        DatabaseFilename = input("What would you like to call this file?\n###Enter a filename.")

##3rd variable
File = Extension + Filename


#Code
e = open(DatabaseExtension+DatabaseFilename,'r')
NameList = e.readlines()
fieldnames = ["firstname","lastname","email"]
e.close()

mergeList = []

for name in NameList:
    fields = name.split(',')
    print(fields)
    n=0
    names = {}
    for field in fields:
        item = field
        names[fieldnames[n]] = item
        n=n+1
    mergeList.append(names)
print(names)

f = open(File,'a')
for x in mergeList:
    var02 = "Dear "+x["firstname"]+" "+x["lastname"]+',Is this your correct email address? '+x["email"]+"\n"
    print(var02)
    f.writelines(var02)
f.close()
