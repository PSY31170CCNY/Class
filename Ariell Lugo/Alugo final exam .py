PSY31170 Winter Session 2019 Final Exam
Ariell Lugo

1. Fix this expression without changing any numbers,  so x evaluates to 28:
	
	
	x = 7*2*2 #note: read the file PythonArithmetic.py for clues
	print x
	
	

2.  initialize p correctly so it prints 10
	
p= 7
for x in range(3):
	p = p + x
print(p)

3.  fix the syntax and logic errors in this code snippet so it prints 101
z= true
	
y=1
while z:
    y+=10
    if y == 101:
        z=false
print(y)

4. Using these variables with the built-in string function str.upper() 
and string slicing,  put an expression into the print statement that 
outputs exactly this:

The quick brown fox jumps over the lazy dog named Rover
	
   s="the quick brown "
f = ["animal", "fox", "puppy"]
j="jumps over 'Rover' the lazy dog"
news=s[0]
s=news+s[1:]
print(s,f[1],j[0:10],j[19:31],j[12:17])
    
5. What command must be executed before you can use the the csv.reader() 
function to read in a text file of values separated by commas?  
Demonstrate by writing a very short program to read in a csv file 
named “data.csv” using the csv.reader() function.
	
	import csv
with open('data.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print (', '.join(row))

6. Debug this program so it runs correctly, print out the resulting file 
with at least 6 users' data and upload the file to your github Class folder:

# finalexamproblem6.py
# Asks user for their information and adds it to a text file 
    
    while tru:
    print ("enter your name, address, and phone please")
    name= input ("Your name")
    addr= input ("Your Address")
    phone= input ("Your Phon")
    entry= (name+addr+phone)
    if name ==":
    	     break
    open(“textfile.txt”,’w’)
    f.writelines (entry+'\n')
    f.close()
