#Assignment Set 1A (abridged).py


#File variables piece
Extension = "C:/Users/aschwar002/Desktop/"
Filename = "email list01.csv"
File = Extension + Filename

#data entry piece
x = True
while x:
    A_is = input("Would you like to enter a new person? Y/N")
    if A_is in "NnNono":
        break
    while A_is in "YyYesyesSure":
        a = input("Enter your last name.")
        if a == "":
            break
        b = input("Enter your first name.")
        if b == "":
            break
        c = input("Enter your email address.")
        if c == "":
            break
        d = str('"'+b+'"'+','+'"'+a+'"'+','+'"'+c+'"'+'\n')
        # notice the order of a and b are swaped
        ## to comply with instructions
        f = open(File,'a')
        f.writelines(d)
        f.close()
        continue
    print("Try again.")
    
