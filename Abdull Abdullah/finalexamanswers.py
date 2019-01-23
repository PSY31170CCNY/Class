#PSY31170 Final Exam

#due  Friday 1/25/2019 by midnight, along with all assignments and the class project

1. Fix this expression without changing any numbers, so x evaluates to 28:
x = 7 * 2* 2
print(x)

2. initialize p correctly so it prints 10
p=()
for x in range(0,11):
	p =  x
print(p)

3. fix the syntax and logic errors in this code snippet so it prints 101
z = True
y=1
while z:
    y+=10
    if y > 100:
        z = False
print(y)

4. Using these variables with the built-in string function str.upper() and string slicing,  put an expression into the print statement that outputs exactly this:
The quick brown fox jumps over the lazy dog named Rover

s = "the quick brown"
f= 'fox'
j= "jumps over the lazy dog named Rover"
print(s,f,j)

5. What command must be executed before you can use the the csv.reader() function to read in a text file of values separated by commas?Demonstrate by writing a very short program to read in a csv file named “data.csv” using the csv.reader() function.

import csv
Reader = csv.reader(open('data.csv', newline=''), delimiter=' ', quotechar='|')
for row in Reader:
    print(', '.join(row))
lol, lol, lol, lol, Bakedziti
LOL, LMAO, ROFLCOPTER

6. Debug this program so it runs correctly, print out the resulting file with at least 6 users' data and upload the file to your github Class folder:
finalexamproblem6.py
Asks user for their information and adds it to a text file 

class person:
    def __init__(self,name=' ',address=' ',phone=' ', email=' '):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
    def hello(self):
        print("enter your name, address, and phone please.")

Abe = person('Abe','city college','911','abe@abe.abe')
Dave = person('Dave','queens college','Example@user.com')
Aleshia = person('Aleshia','lala land','Example@user.com')
Alex = person('Alex','saman ave','Example@user.com')
Ariel = person('Ariel','123 40th rd','Example@user.com')
Briona = person('Briona','creole banks','Example@user.com')

Abe.hello()
while True:
    name = input('Your name : ')
    addr = input('Your address : ')
    phone = input('Your phone : ')
f.writelines(name,addr,phone)
f.close()
if name == '':
    print("Cool, now go home")

Dave.hello()
Aleshia.hello()
Alex.hello()
Ariel.hello()
Briona.hello()

people = [Abe,Dave,Aleshia,Alex,Ariel,Briona]


print(people)
