# Personclass.py

class Person:
    def __init__(self,name=' ',address=' ',phone='',email=''):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def hello(self):
        print("Hi there! My name is ",self.name)


Sally = Person('Sally','1 Any Way','123-4567','sally@gmail')

print(Sally.name)

Sally.hello()

#instantiate a Person in the variable Bob, named "Robert" 
Bob = Person("Robert",'1234 Drive',email='bob@gmail')
Bob.hello()

#make a list of the People objects:
people=[Bob,Sally]
drive='/Downloads/Personclass.py
#write the name and emails of the people to a csv file for Excel:
e=open('/media/dave/PSY31170/emaillist.csv','w') #open the file
for member in people:
    # construct the text line for each member:
    # put the attributes in quotes separated by a comma,
    # like this: "Dave","dave@gmail"
    # add a newline at the end so each entry is on a new line
    l='"' + member.name + '"' + ',"' +member.email+ '"\n'
    e.writelines(l)
e.close()

# now read the file and see what it looks like:
e=open('/media/dave/PSY31170/emaillist.csv','r')
print("......\nread one line at a time and print it:")
print("each entry has a newline at the end, and the print function adds another one.")
for l in e: #e is a file object, so this reads the file one line at a time
    print (l) # show the line that was just read
e.close() # close the file to keep the operating system happy
      
# or
print ("------\nthe whole file as a list:")
e=open('/media/dave/PSY31170/emaillist.csv','r') # notice 'r' for read, not 'w' for write
emails=e.readlines() # gets all the lines into memory, for small files
print (emails)
      
# or
print ("-----\none item in the list at a time (without the newlines):")
for l1 in emails: # each l1 is one line 
    print(l1[0:-1]) # slice off the last char to remove the trailing newline

e.close() # close the file to keep the operating system happy    

# let's read the file in as a python dictionary, so we can look up entries by name
e=open('/media/dave/PSY31170/emaillist.csv','r')
peopledict = {} # initialize an empty dictionary
for p in e:
    # each p is one line from the excel format csv filefile
    # so it is a text string of a list of attribute values:
    print('text string of this line:',p)
    print('length of text string:',len(p))
    # use split to separate the values:
    pvals = p.split(',') # separates by commas
    # use the first one as the key to look up by and the second as the
    # value that the key is associated with:
    print('Now the text string is made into a list separated by commas:',pvals)
    print('The full read-in entry text line is now a list of',len(pvals),'items long')
    # now put the entry into the dictionary:
    peopledict[pvals[0]] = pvals[1] #pvals[0] is the name, pvals[1] is the email
e.close()

# now see what we have in the dictionary peopledict:
print("\nThe raw peopledict is:\n",peopledict)
print ("--- now displayed by key-value pairs:")
for p in peopledict.keys():
    print ("lookup key:",p,"value:",peopledict[p][0:-1]) #take off trailing \n
print('===\n')
n=''
while n == '':
    n=input("Go ahead, enter a name to look up their email:")
    try: # the try-except block catches errors without crashing the program
        print(peopledict['"'+n+'"']) # add the quotes present for csv format
    except:
        print("Error: ",n,"not found in peopledict. Try again.")
        n=''
        
# === TO DO: ===
"""
1. Add a user data entry loop to allow more names and emails to be entered.
    Include the entry of the other data attributes of a Person
2. Add more attributes,but leave the data entry for now
3. add a loop to let the user look up an entry by name, and then enter a value
    for another attribute if the dictionary entry is found.
4. After any new data is entered, re-write the csv file to save the data.


"""
    
    
