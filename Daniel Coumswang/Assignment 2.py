e=open('emaillist.csv','r')
w=e.readlines()
   
for names in w:
   x=  names.split(",")
   print("Dear " + x[0][1:-1] + " " + x[1][1:-1] + ". " + "Is this your email address?" +x[2][1:-1] ) 
