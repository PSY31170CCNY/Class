e=open('saved_tweetsTrump.csv','a')
columnTitleRow = '"'+x+'", "' +l+'", "'+ w+"\n"
e.write(columnTitleRow)
e=open('saved_tweetsTrump.csv','r')
w=e.readlines()

x= input('welcome type in word to search text')
print(x)




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
    
