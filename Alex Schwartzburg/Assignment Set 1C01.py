#Assignment Set 1A

Extension = "C:/Users/aschwar002/Desktop/"
Filename = "apikeys.csv"
File = Extension + Filename


x = True
while x:
    var1 = input("Would you like to enter a new api key name? Y/N")
    if var1 == 'N':
        break # maybe we want to call up a "main menu"
    while var1 in "YyYesyesSure":
        var01 = input("Enter the api key name.")
        if var01 == "":
            break
        var02 = str('"'+var01+'\n')
        # notice the order of var01 and var02 are swaped
        ## to comply with instructions
        f = open(File,"a")
        f.writelines(var02)
        f.close()
        continue
    print("Try again.")
