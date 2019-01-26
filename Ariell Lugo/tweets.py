import csv

# creating dictionaries
textStrings = { }
locations = { }
with open('tweets.csv', 'r') as IN:
   reader = csv.reader(IN, delimiter=',')
   for line in reader:
       if len(line) < 4: # ignores lines that don't have 4 coulumns
           continue
       text = line[ 1 ] 
       location = line[ 3 ]
       name = line[2]
       # dictionary from text string to its location
       textStrings[ text ] = location
       # dictionary from location to its text string
       locations[ location ] = text


searchString = input('Enter search string: (or q to quit):').lower()

while searchString != 'q':
    searchBy = input('Enter t to search by text or l to search by location:').lower()
    if searchBy == 't':
        dictToSearch = textStrings #searching by text
    else:
        dictToSearch = locations #searching by location
        
    for key in dictToSearch:
        words = key.split()
        for i in range(len(words)):
            words[i] = words[i].lower()
        if searchString in words:
            if searchBy == 't':
               print('Text: {0}, Location: {1}'.format(key, textStrings[key])) #key is text, value is location
            else:
               print('Text: {1}, Location: {0}'.format(key, locations[key])) #key is location, value is text
            # must ask again because you need the option to stop
    searchString = input('Enter search string: (or q to quit):').lower()
    
    

