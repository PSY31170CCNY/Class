#puts tweets in csv file and reads through it
e=open('saved_tweetsTrump.csv','a')
columnTitleRow = '"'+x+'", "' +l+'", "'+ w+"\n"
e.write(columnTitleRow)
e=open('saved_tweetsTrump.csv','r')
w=e.readlines()

x= input('welcome type in word to search text')
print(x)
#displays tweets from string requested
with open(datafile, newline='') as csvfile:
datareader = csv.reader(csvfile,delimiter = ',', quotechar='|')
n+=1
        try:
            print(n,row)
        except Exception as e:
print(n,'failed due to ',str(e))

for tweettext in alltext:
    try:
        x=tweettext.find('asdf')
        print('asdf is at position',x)
    except Exception as e: # creates a variable e that holds the Exception object
        print("oops! error: ", str(e)) # displays the error message from e
	# do something to compensate for the error if possible
        continue # then go on to the next line, don't keep processing

    # if the try block worked, do whatever tweettext[x] needs to have done, e.g.
    print('asdf appears at position ',x, ' in ',tweettext)
    

    
