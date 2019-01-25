#1
x=7 * 2 * 2
print(x)

#2
p=7
for x in range(3):
    p = p+x
print(p)

#3
z=True
y=1
while z:
    y+=1
    if y > 100:
        z=False
print(y)

#4
s="The quick brown"
f=['animal','fox','puppy']
j='jumps over "Rover" the lazy dog'
print(s+' '+f[1]+' '+j[0:11]+j[19:]+' named '+j[12:17])

#5
import csv
Reader = csv.reader(open('data.csv'))
for row in Reader:
    print(', '.join(row))

#6
while True:
    def info(name, address, phone):
        print("Your name is: ",name)
        print("your address is: ",address)
        print("your phone number is: ",phone)

    print("*"*70)
    print("Enter your name, address, and phone number, please. ")
    name=input("Your name: ")
    address=input("Your address: ")
    phone=input("Your phone: ")

    print("-"*70)

    with open("textfile.txt", "a") as f:
        f.write('\n' +name+ " "+address+" "+phone)
        info(name, address, phone)

        print("if you want to stop the program, enter 1. To enter another profile press ENTER.")
        end = input()
        if end=="1" :break
        else: continue
