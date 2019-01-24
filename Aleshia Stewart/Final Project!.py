# final exam
# Aleshia Stewart

x = 7 * 2 * 2
print(x)

#2 answer
p = 7
for x in range(3):
    p = p + x
print(p)

#3 answer
z= True
y=1
while z:
    y+=1
if y == 100:
    z=False
print(y+1)

#4 answer
s="the quick brown"
f=['animal', 'fox', 'puppy']
j='jumps over "Rover" the lazy dog'
print (s.capitalize()+' '+f[1]+' '+j[0:11]+j[19:]+' named '+j[12:17])

#5 answer
e=open('data.csv','r')
w=e.readlines()

#6 answer
# finalexamproblem6.py
# Asks user for their information and adds it to a text file 
while True:
    print("Enter your name,, address and phone, please")
    name = input('Your name')
    addr = input('Your address')
    phone=input("Your phone")
    f = open("textfile.txt",'a')
    f.writelines(name+' '+addr+' '+phone+"\n")
f.close()







