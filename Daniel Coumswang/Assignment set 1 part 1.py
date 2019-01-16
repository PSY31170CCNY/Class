#Assignment set 1 part 1

x = True
while x:
    print("Please enter your information.")
    A = input("Enter your first name:")
    b = input("Enter your last name:")
    c = input("Enter your Email:")

    d = open('emaillist.csv','a')
    e =  '"'+A+'", "' +b+'", "'+c+"\n"
    d.write(e)

