#Assignment Set 1A

Extension = "C:/Users/aschwar002/Desktop/01.15.2019/"
Filename = "email list.csv"
File = Extension + Filename


x = True
while x:
    var1 = input("Would you like to enter a new person? Y/N")
    if var1 == 'N':
        break # maybe we want to call up a "main menu"
    while var1 in "YyYesyesSure":
        var01 = input("Enter your last name.")
        if var01 == "":
            break
        var02 = input("Enter your first name.")
        if var02 == "":
            break
        var03 = input("Enter your email address.")
        if var03 == "":
            break
        var04 = str('"'+var02+'",'+'"'+var01+'",'+var03+'\n')
        # notice the order of var01 and var02 are swaped
        ## to comply with instructions
        f = open(File,"a")
        f.writelines(var04)
        f.close()
        continue
    print("Try again.")



