names = []
while True:
    last_name = input("enter last name:")
    if last_name == "":
        break
    first_name = input("enter first name:")
    if first_name == "":
        break
    email = input("enter email:")
    print(last_name)
    print(first_name)
    print(email)
    
entries=[last_name,first_name,email]
drive='/media/ware/PSY31170/'
filename = input("enter a file name:")
e=open(drive+filename,'r')
print("dear", first_name,last_name,", is this you correct email address?",1)
e.close()

from twython import twython
credentials['last_name']
credentials['first_name']
credentials['email']
with open("twitter_credentials.json","w")as file:
    Json.dump(credentials,file)
with open("twitter_credentials.json","r") as file:
     creds = json.load(file)
python_tweets=Twython(creds['last_name'],creds['first_name'],creds['email']
query={'q':'tweets','result_type':'popular','coumt':100,'lang':'en',}

                 
