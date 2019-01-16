#Assignment Set 1B (updated 1/16/2019)

#Variable assignments
##First Choice
var1 = input("Would you like to create a new file or use the default? \n1 - Use Default.\n2 - Create new file.")
#if var1 = 1, use default.
while var1 == "":
    var1 = input("Would you like to create a new file or use the default? \n1 - Use Default.\n2 - Create new file.")
if var1 == '1':
    Extension = "C:/Users/aschwar002/Desktop/"
    Filename = "FormLetter.txt"
elif var1 == '2':
    Extension = input("Where would you like to create your file?\n###Enter the file path.")
    Filename = input("What would you like to call this file?\n###Enter the filename.")

##2nd Choice - which database do you want to use?
var2 = input("Would you like to use the default database or call a new one? \n1 - Use Default.\n2 - Create new file.")
###if var2 = 1, use default.
while var2 == "":
    var2 = input("Would you like to use the default database or call a new one? \n1 - Use Default.\n2 - Create new file.")
if var2 == '1':
    DatabaseExtension = "C:/Users/aschwar002/Desktop/"
    DatabaseFilename = "email_list.csv"
elif var2 == '2':
    DatabaseExtension = input("Where is the database?\n###Enter a file path.")
    DatabaseFilename = input("What would you like to call this file?\n###Enter a filename.")

##3rd variable
File = Extension + Filename


#Code
e = open(DatabaseExtension+DatabaseFilename,'r')
NameList = e.readlines()
e.close()

mergeList = []

for A in NameList:
    names = A.split(',')
    mergeList.append(names)
        
print(names)

f = open(File,'a')
for x in mergeList:
    var02 = "Dear "+x[0]+" "+x[1]+',Is this your correct email address? '+x[2]+"\n"
    print(var02)
    f.writelines(var02)
f.close()
