1.Fix this expression without changing any numbers,  so x evaluates to 28:
	x = 7 * 2  **2   
Answer
x = 7 * (2  **2)

2.  initialize p correctly so it prints 10
p= ???
for x in range(3):
	p = p + x
print(p)

Answer

p= 7
for x in range(3):
	p = p + x
print(p)


3.  fix the syntax and logic errors in this code snippet so it prints 101
z= true
y=1
while z:
    y=y+1
    if y == 100:
        z= False
print(y)


Answer
z= True
y=1
while z:
    y=y+1
    if y == 100:
        z= False
print(y)



4. Using these variables with the built-in string function str.upper() 
and string slicing,  put an expression into the print statement that 
outputs exactly this:

The quick brown fox jumps over the lazy dog named Rover

    s=”the quick brown”
    f=[‘animal’, ‘fox’, ‘puppy’]
    j=’jumps over “Rover” the lazy dog’
   print (?????)

Answer:
s="the quick brown "
f = ["animal", "fox", "puppy"]
j="jumps over 'Rover' the lazy dog"
news=s[0]
news=news.upper()
s=news+s[1:]
print(s,f[1],j[0:10],j[19:31],j[12:17])

    
5. What command must be executed before you can use the the csv.reader() 
function to read in a text file of values separated by commas?  
Demonstrate by writing a very short program to read in a csv file 
named “data.csv” using the csv.reader() function.
Answer 

import csv
with open('data.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print (', '.join(row))

6.F= open("textfile.txt",'w')
while True
print("enter your name, address and phone,please")
name = input("your name")
address = input ("your address")
phone = input ("your phone")
f.writelines(name,address,phone)
if name=="":
    break f.close()
