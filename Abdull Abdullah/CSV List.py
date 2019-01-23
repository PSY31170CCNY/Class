# ASSIGNMENT 1.PY
# DAVE BRITTON
# CREATE A USER-ENTERED CSV LIST OF NAMES AND EMAIL ADDRESSES
class humans:
    def __init__(self,name=' ',lastname=' ',email=''):
        self.name = name
        self.lastname = lastname
        self.email = email
    def hello(self):
        print("Hi, what is your name?")

Abdull = humans('abdull','abdullah','abdull@gmail')

Abdull.hello()
while True:
    answer = input()
    print("Cool, now what's your last name?")
    r = input('')
    print("Awesome, and now your email address?")
    pepe = input('')
    print("Thank you, you may now leave.")
    
Abdull = humans('abdull','abdullah','abdull@gmail')
Dave = humans('Dave','britton','Example@user.com')
Aleshia = humans('Aleshia','stewart','Example@user.com')
Alex = humans('Alex','schwartzburg','Example@user.com')
Ariel = humans('Ariel','lugo','Example@user.com')
Briona = humans('Briona','couloote','Example@user.com')
Daniel = humans('Daniel','coumswang','Example@user.com')
Jamin = humans('Jamin','chowdhury','Example@user.com')
Jason = humans('Jason','joseph','Example@user.com')
Oluwatobi = humans('Oluwatobi','kolawale','Example@user.com')
Justin = humans('Justin','pearce','Example@user.com')
Ramon = humans('Ramon','brito','Example@user.com')
Stephanie = humans('Stephanie','bodden','Example@user.com')
Ware = humans('Ware','Astin','Example@user.com')

Abdull.hello()
Dave.hello()
Aleshia.hello()
Alex.hello()
Ariel.hello()
Briona.hello()
Daniel.hello()
Jamin.hello()
Jason.hello()
Oluwatobi.hello()
Justin.hello()
Ramon.hello()
Stephanie.hello()
Ware.hello()

people = [Abdull,Dave,Aleshia,Alex,Ariel,Briona,Daniel,Jamin,Jason,
               Oluwatobi,Justin,Ramon,Stephanie,Ware]

print(people)
