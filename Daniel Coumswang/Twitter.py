import csv
datafile="saved_tweetsTrump.csv"
n=0
with open(datafile, newline='') as csvfile:
    datareader = csv.reader(csvfile,delimiter = ',', quotechar='|')
    for row in datareader:
        n+=1
        try:
            print(n,row)
        except Exception as e:
            print(n,'failed due to ',str(e))
