while True:
    print("Enter your name,, address and phone, please")
    f = open("textfile.txt",'a')
    name = input('Your name')
    addr = input('Your address')
    phone=input("Your phone")
    f.writelines(name+' '+addr+' '+phone+"\n")
    f.close()
    if name=='':
         break

