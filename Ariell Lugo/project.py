# analysis of libraries open on a sunday :D 
# file: Queens_Library_Branches.csv
import csv  #gets the module

# The data dictionary can be found in the spreadsheet file at this link:
# https://data.cityofnewyork.us/Education/Queens-Library-Branches/kh3d-xhq7
# We did not use all the columns in the data but they are:
name=0 #used
addres=1 #used
city=2 #notused
postcode=3 #notused
phone=4 #used
Mn=5 #notused
Tu=6 #notused
We=7 #notused
Th=8 #notused
Fr=9 #notused
Sa=10 #notused
Sun=11 #used
Notification=12 #notused
Location1=13 #notused
Borough=14#notused
Latitude=15 #notused
Longitude=16 #notused
Community Board=17 #notused
Council District=18 #notused
BIN=19 #notused
BBL=20 #notused
NTA=21 #notused


class Library(object):
    def __init__(self, name, address, phone, sundayHours):
        self.name = name
        self.address = address
        self.phone = phone
        self.sundayHours = sundayHours

    def isOpenOnSunday(self):
        if 'Closed' in self.sundayHours:
            return False
        else:
            return True

    # just a function to print out the info for the library
    def printInfo( self ):
        print('Name = {0}, Address = {1}, Phone = {2}, Hours = {3}'.format(\
                self.name, self.address, self.phone, self.sundayHours))

# We will have two dictionaries.  One containing the libraries that are
# open on Sundays and one containing those that are closed.
# The key will be the library name.  The value will be the library object.
openOnSundays = {}
closedOnSundays = {}

with open('libraries.csv', 'r') as INPUT:
    reader = csv.reader(INPUT, delimiter=',')
    #for line in INPUT:
    #    print(line)
    count = 0 # counter gets updated for each line read
    for line in reader:
        if count == 0: # skip the header line
            count = count + 1 
            continue
        name = line[0]
        address = line[1]
        phone = line[4]
        sundayHours = line[11]
        #print('sunday hours = ', sundayHours)
        count = count + 1 # we always increment the counter
        library = Library(name, address, phone, sundayHours)
        if library.isOpenOnSunday(): # if True, add to the open libraries dictionary
            openOnSundays[ name ] = library
        else:
            closedOnSundays[ name ] = library

print('OPEN ON SUNDAYS: ')
# Now, let's print all libraries that are open on Sundays
for name in openOnSundays:
    library = openOnSundays[ name ]
    library.printInfo()
#Enter library name and see if it's open on sunday's in the openonsundays dictionary.
name = input('Enter name (or q to quit):').title()
while name != 'Q':
    if name in openOnSundays:
        library = openOnSundays[name]
        print('{0} is open on Sundays: {1}'.format(name, library.sundayHours))
    else:
        print('{0} is closed on Sundays'.format(name))
    name = input('Enter name (or q to quit):').title()
        
            
        
## i was able to determine that the libraries in queens open on a 
#  sunday are Central Library, Cyber center, flushing, job information center,
#  and kew gardens hills. i can also search and see if a particular library name listed
#  in the data is open or closed on sundays. 
        
