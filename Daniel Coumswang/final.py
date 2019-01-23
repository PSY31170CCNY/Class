#1
x=7*2 *2
print(x)

#2
p=7
for x in range(3):
    p=p+x
print(p)

#3
z=True
y=1
while z:
    y+=1
    if y == 100:
        z=False
print(y+1)

#4
s="the quick brown"
f=['animal','fox','puppy']
j='jumps over "Rover" the lazy dog'
print(s.capitalize()+' '+f[1]+' '+j[0:11]+j[19:]+' named '+j[12:17])

#5
k = open('data.csv','r')
w=k.readlines()

#6
while True:
    print("Enter your name, address, and phonenumber, please")
    name = input("Your name: ")
    addr = input("Your address ")
    phone = input("Your phone number: ")
    b = open('textfile.txt','a')
    b.writelines(name+' '+addr+' '+phone+"\n")
    b.close()
    

