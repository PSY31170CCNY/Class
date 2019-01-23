while True:
    print('welcome User please put in your information.')

    x = input("First Name:")
    print(x)
    l=input("Last Name:")
    print(l)
    w=input("email:")
    print(w)


    e=open('emaillist.csv','a')
    #   "dave", "Britton", "dave@gmail\n"
    #   "x", "l", "w\n"
    columnTitleRow = '"'+x+'", "' +l+'", "'+ w+"\n"
    e.write(columnTitleRow)


	
