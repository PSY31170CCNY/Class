#StockData Version 12
#by Alex Schwartzburg
# you will neeed to download the file paths and 

Input1 = input("Please enter the filepath to where you have downloaded the provided csv files.")
Input2 = input("Please enter the filepath to where you want the output file to go.")


#Imported Modules
import pandas as pd


#Dictionaries
linksDict = {'GSPC':"https://finance.yahoo.com/quote/%5EGSPC/history?period1=-630961200&period2=1547960400&interval=1d&filter=history&frequency=1d",
             'IXIC':"https://finance.yahoo.com/quote/%5EIXIC/history?period1=-630961200&period2=1547960400&interval=1d&filter=history&frequency=1d",
             'DJI' :"https://finance.yahoo.com/quote/%5EDJI/history?period1=-630961200&period2=1547960400&interval=1d&filter=history&frequency=1d"
             }

pathsDict = {'GSPC':Input1, # Edit this
             'IXIC':Input1, # Edit this
             'DJI' :Input1, # Edit this
             'master':Input2  # Edit this
             }

nameDict  = {'GSPC':'^GSPC-5.csv',
            'IXIC' :'^IXIC-5.csv',
            'DJI'  :'^DJI-5.csv',
            'master':'Master.csv'
            }

KeyLookup = ['GSPC', 'IXIC', 'DJI']
Index = ['GSPC', 'IXIC', 'DJI']
fieldname = ['Date','Open','High','Low','Close','Adj Close','Volume']
fieldname2 = ['index','Date','Open','High']


#Files

file1 = open(pathsDict['GSPC']+nameDict['GSPC'],'r')
file2 = open(pathsDict['IXIC']+nameDict['IXIC'],'r')
file3 = open(pathsDict['DJI']+nameDict['DJI'],'r')
file4 = open(pathsDict['master']+nameDict['master'],'w')
file5 = open(pathsDict['master']+nameDict['master'],'r')
#COMMENT_1
#   pandas crashes if you don't put
#   a raw text string of the form
#   '/Users/Username/Desktop/Master.csv'
#   for file5 and for the csv reader down below.

#Code
 # do one of these for File1, File2, File3 
file1
data1 = file1.readlines()
file1.close()

file2
data2 = file2.readlines()
file2.close()

file3
data3 = file3.readlines()
file3.close()


#open up a csv file
#read a row from it
#peel off the relevant fields

GSPC = []
IXIC = []
DJI  = []

#ELIMINATE THE '\n'
for x in data1[0:len(data1)]:
    a = x.split('\n')
    GSPC.append(a[0])
    
for x in data2[0:len(data2)]:
    a = x.split('\n')
    IXIC.append(a[0])

for x in data3[0:len(data3)]:
    a = x.split('\n')
    DJI.append(a[0])

GSPCdate = ['GSPC ']
GSPCadjclose = ['GSPC ']
GSPCvolume = ['GSPC ']

IXICdate = ['IXIC ']
IXICadjclose = ['IXIC ']
IXICvolume = ['IXIC ']

DJIdate = ['DJI ']
DJIadjclose = ['DJI ']
DJIvolume = ['DJI ']



#CREATE FIELDS
for x in GSPC:
    b = x.split(',')
    GSPCdate.append(b[0])
    GSPCadjclose.append(b[5])
    GSPCvolume.append(b[6])

    
####
for x in IXIC:
    c = x.split(',')
    IXICdate.append(c[0])
    IXICadjclose.append(c[5])
    IXICvolume.append(c[6])
    

####
for x in DJI:
    d = x.split(',')
    DJIdate.append(d[0])
    DJIadjclose.append(d[5])
    DJIvolume.append(d[6])


#Outputting the data into a list 
NewList = []
for x in range(len(data3)):
    Z = str(
        '"'+GSPCdate[x]+'",'+'"'+IXICdate[x]+'",'+'"'+DJIdate[x]+'",'+
        '"'+GSPCadjclose[x]+'",'+'"'+IXICadjclose[x]+'",'+'"'+DJIadjclose[x]+'"\n'
        )
    NewList.append(Z)

#export NewList to a file called 'Master.csv'
for x in NewList:
    file4.write(x)
file4.close()

#open the file in read mode (avoid crashing the program)
file5
data5 = file5.readlines()


e = pd.read_csv(open(Input2+'Master.csv','r'),header=[0,1])
#see COMMENT_1

Explanation = '''\n\n\nThe financial indices of a society serve many measurement functions.
Indices are often used as benchmarks against which to compare the performance of investment portfolios.

It is therefore interesting to examine the strength of the relationships of
one index to another.
It would be even more interesting to correlate the changes
in an index with the changes in another.
This program extracts historical data for each index
from quote.yahoo.com, exports it into a single csv file, and then uses the
'pandas' module to run correlations on the adjusted closing prices of the three indices.

Ultimately it is shown that all three indices are VERY strongly correlated.

That said, this program was designed with hopes for expansion.
Future updates would include:
1. The ability to update the batches of historical data,
   automatically by accessing yahoo directly.
2. Expanded statistical calculations callable from within the interface.
3. The addition of other indices, for example the Russell 2000.
4. A tool that calculated the correlation among the CHANGES in an index's
value, not just the value itself.
\n\n\n'''



#data entry piece
run = True
while run == True:
    A_is = input("Are you curious about the stock market? Y/N")
    if A_is in "NnNono":
        break
    while A_is in "YyYesyesSure":
        a = input("""Please select one of the following options.
\n1 - Read what the purpose of this program is.
\n2 - Review source documentation.
\n3 - View the correlation between the three most popular financial indices.""")
        if a == "":
            break
        else:
            if a == '1':
                print(Explanation)
                input('Press enter to return to start')
                break
            else:
                if a == '2':
                    b = input('''\n\n
=========================================================
\nMarket data for the following indices has been downloaded
from yahoo.com and is current as of 1/18/2019
\nLinks to the current data have been provided.
\nWhich index would you like to link to?
\n1 - GSPC (Standard & Poors)
\n2 - IXIC (Nasdaq)
\n3 - DJI  (Dow Jones Industrial Average)''')
                    if b == '1':
                        print('\n\n\nThe historical data for GSPC was retrieved from:\n\n'+linksDict['GSPC']+'\n\n')
                        input('Press enter to return to start')
                        break
                    else:
                        if b == '2':
                            print('\n\n\nThe historical data for IXIC was retrieved from:\n\n'+linksDict['IXIC']+'\n\n')
                            input('Press enter to return to start')
                            break
                        else:
                            if b == '3':
                                print('\n\n\nThe historical data for DJI was retrieved from:\n\n'+linksDict['DJI']+'\n\n')
                                input('Press enter to return to start')
                                break
                else:
                    if a == '3':
                        print('Hello! The correlations you want are as follows.\n\n')
                        print(e.corr('pearson',1))
                        print('\n\n')
                        input('Press enter to return to start')
                        break                            
                            
                            
##    print("Try again.")               
file5.close()


