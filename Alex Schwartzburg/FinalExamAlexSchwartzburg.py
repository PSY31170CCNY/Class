#PSY31170 Winter Session 2019 Final Exam
#Completed by ALEX SCHWARTZBURG

#due  Friday 1/25/2019 by midnight, 
#along with all assignments and the class project

# "Welcome to Alex's final exam.
#    This was designed to be read as output in python shell.
#      You are about to begin your review.  You can do it here or in the shell
#       Sit back and enjoy!
#      …And then scroll to the top and slog through." —Alex



print("""Welcome to Alex's final exam.
      Please read everything in its output form in python shell.
      You are about to begin your review.
      Sit back and enjoy!
      And then scroll to the top and slog through.
      Thanks for a great semester! -Alex""") 



#Question 1
print("""\n\n\n
============================================================================
1. Fix this expression without changing any numbers,so x evaluates to 28:
x = 7 * 2  **2\n\n While the answer may APPEAR TO BE to do nothing,
as x will evaluate to 28 anyway, this only occurs
because 2x2 = 2^2 = 4.
For the majority of numbers, however, it would
be necessary to eliminate one of the asterisks from the double asterisk
to obtain
x = 7 * 2 * 2
, because ** means exponentiation in python. 
Also, the expression was indented.  So I needed to de-indent it.
The corrected expression appears in my code on the next line.""")
x = 7 * 2 * 2


#Question 2
print("""2.  initialize p correctly so it prints 10

p= ???
for x in range(3):
	p = p + x
print(p)

##'Alex says: "set p = 7"')
The code demonstrating this works
is on the next few lines and will evaluate in < 1 second.""")
p=7
for x in range(3):
	p = p + x
print(p)

#Question 3
print("""\n\n\n\n
============================================================================
3.  fix the syntax and logic errors in this code snippet so it prints 101
z= true
y=1
while z:
    y+=10
    if y = 100:
        z=false
print(y)""")

print("""the repaired code would look like this:
z = True
y = 1
while z:
    y += 1
    print(y)
    if y == 101:
        z = False

and it would result in the following list of numbers: [see output in shell]      """)

z = True
y = 1
while z:
    y += 1
    print(y)
    if y == 101:
        z = False

print("""\n\nIt should be said however, that you could just do.\n\ny = 101
print(y)\n which would output this: """) 
y = 101
print(y)

#Question 4
print("""\n\n\n\n
============================================================================
4. Using these variables with the built-in string function str.upper()
and string slicing,  put an expression into the print statement that 
outputs exactly this:

  The quick brown fox jumps over the lazy dog named Rover
s="the quick brown"
f=['animal', 'fox', 'puppy']
j='jumps over "Rover" the lazy dog'

print(str.upper(s[0])
      +str.lower(s[1:len(s)])
      +s[3]+f[1]+s[3]
      +j[0:10]
      +j[-13:]
      +s[3]+s[14]+j[-7]+j[2]+s[2]+j[-3]+s[3]
      +j[12:17])

""")  

s="the quick brown"
f=['animal', 'fox', 'puppy']
j='jumps over "Rover" the lazy dog'

print(str.upper(s[0])
      +str.lower(s[1:len(s)])
      +s[3]+f[1]+s[3]
      +j[0:10]
      +j[-13:]
      +s[3]+s[14]+j[-7]+j[2]+s[2]+j[-3]+s[3]
      +j[12:17])

#Question5
print("""\n\n\n\n
============================================================================
5. What command must be executed before you can use the the csv.reader() 
function to read in a text file of values separated by commas?  
Demonstrate by writing a very short program to read in a csv file 
named “data.csv” using the csv.reader() function.""")

print("""you have to import the csv module.
so,



'import csv'




""") 


#Question 6
print("""\n\n\n\n
============================================================================
6. Debug this program so it runs correctly, print out the resulting file 
with at least 6 users' data and upload the file to your github Class folder:


# finalexamproblem6.py
# Asks user for their information and adds it to a text file 
while True
print(Enter your name,, address and phone, please)
f = open(“textfile.txt”,’w’)
name = ‘input(Your name’)
addr = input’((Your address’)
phone=’input(Your phone)’
f.writelines(name,add,phone)
f.close()
if name=’’:
break

Actual code executes below.\n\nWelcome to the program in question 6.\n\n""")

# finalexamproblem6.py
# Asks user for their information and adds it to a text file 

path = input("""please type the filepath to your desktop
or an alternative place where you plan to save
your output file. Remember to properly include all forward slashes.""")
condition = True
while condition == True:
      f = open(path+'textfile.txt','a')
      name = input('Enter your name please.')
      addr = input('Enter your address.')
      phone= input('Your phone?')
      string = '"'+name+'",'+'"'+addr+'",'+'"'+phone+'"\n'
      f.writelines(string)
      f.close()
      if name=='':
          break
