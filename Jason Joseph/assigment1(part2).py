#Assignment Number 2
#Jason Joseph


DBExtension = "C:/Users/jjoseph005/Desktop/"
DBFilename = "personaldata.csv"
DBFile = DBExtension+DBFilename

Extension ="C:/Users/jjoseph005/Desktop/"
Filename="therealstuff.txt"
File= Extension+Filename

prompt=input("Would you like to have a file with the form letter?(Y/N)")

while  prompt == "Y":
    e = open(DBFile,'r')
    NameList = e.readlines()
    e.close()
    mergeList = []
    for A in NameList:
        names = A.split(',')
        print(names)
        mergeList.append(names)

    f = open(File,'a')
    for x in mergeList:
        var02 = "Dear "+x[1]+" "+x[0]+',Is this your correct email address? '+x[2]
        print(var02)
        f.writelines(var02)
    f.close()
    break
else:
    prompt == "N"
    print ("Cool maybe next time then!")
    
           







