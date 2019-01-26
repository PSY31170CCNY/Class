
#PSY31170 Winter Session 2019 Final Exam


1. Fix this expression without changing any numbers,  so x evaluates to 28:
	x = 7 * 2  **2



--------------------------------------
Answer: 	x = 7 * (2 **2)



#-----------------------------------------------------------------
    
2.  initialize p correctly so it prints 10
p= ???
for x in range(3):
	p = p + x
print(p)

--------------------------------------
Answer:
    p = 7 #Initial value
    p = p +x
    p1 = 7 + 0 = 7
    p2 = 7 + 1 = 8
    p3 = 8 + 2 = 10

    print(p) = 10



#-----------------------------------------------------------------



3.  fix the syntax and logic errors in this code snippet so it prints 101
z= true
y=1
while z:
    y+=10
    if y = 100:
        z=false
print(y)


------------
Answer:
    
z = True
y = 1
    while z:
        y += 10
        print(y)
    if y == 101:
        z = False


#--------------------------------------------------------------------------
        
4. Using these variables with the built-in string function str.upper() 
and string slicing,  put an expression into the print statement that 
outputs exactly this:

The quick brown fox jumps over the lazy dog named Rover

    s=”the quick brown”
    f=[‘animal’, ‘fox’, ‘puppy’]
    j=’jumps over “Rover” the lazy dog’
   print (?????)

-------------------------
Answer:
print(s + f[2] + j[3:5] + 'named' + j[2])

#---------------------------------------------------------------------


5. What command must be executed before you can use the the csv.reader() 
function to read in a text file of values separated by commas?  
Demonstrate by writing a very short program to read in a csv file 
named “data.csv” using the csv.reader() function.

--------------
Answer:

File = FinalExam.csv
open(File, newline='') as csvfile:
    datareader = csv.reader

#-----------------------------------------------------------------------



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


Answer: -----------------------------------------------------------------
Answer:




Destination: "C:/Users/Jamin/Desktop/"
Filename: "Problem_6.txt/"
textfile = Destination + Filename
#Must create textfile before running the program.

print("Enter your name,, address and phone, please")

f = open(textfile, 'w')
name = input("Your name")  
addr = input("Your address")
phone= input('Your phone')
              
f.writelines(name,add,phone)
f.close()
if name == "" :
    break






              
