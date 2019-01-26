#Locate and Generate
Destination = "C:/Users/Jamin/Desktop/Pythass3/"
Filename = "saved_tweetsTrump.csv"
File = Destination + Filename
#-----------------------------------------------------

#Ask the Task
begin = input("Do you want to view the Tweets on Donald Trump? Y/N")
while begin in "Yy":
#Referring to the saved_tweetsTrump.csv created by Dave Britton. 
    v1 = input("We are now going to lauch the spreadsheet, okay? Y/N")
    while v1 == "Yy": 
        v1 = input("Let’s go!")
    if v1 == '':
#-------------------------------------------------------

        Trump = open(Destination+Filename,'r')
        FormList = Trump.readlines()
        Trump.close()
#Opens saved_tweetsTrump.csv

#-------------------------------------------------------

    mergeList = []

    for things in TrumpList:
        listparts = things.split(',')
        mergeList.append(listparts)
            
    print(TrumpList)
#-------------------------------------------------------

Destination2 = "C:/Users/Jamin/Desktop/Pythass3/"
Filename2 = "Trump Tweets.txt"
FormFile = Destination2 + Filename2

#Printing the Trump Tweets text file.
#--------------------------------------------------------

f = open(TrumpFile,'a')
#Opens the Text File in which the TrumpList will be generated.
for formparts in mergeList:
     
        Trump.writelines(v3)
Trump.close()






