import random
cards= []
suits=["hearts" , "spades","diamonds","clubs"]
numbers=["Ace","King","Queent","Jack","10","9","8","7","6","5","4","4","3","2","Ace"]
for suit in range(len(suits)):
    for num in range(len(numbers)):
        cards.append((numbers[num]," of ", suits[suit]))

random.shuffle(cards)

gameover = False
startcard = 0
while not gameover:
       playerhand = cards[startcard:startcard+2]
       startcard = startcard + 1 # or +=1
       print(playerhand)
       hitme='x'
       stop='a'
       while hitme not in ["YyNn"]:
          hitme = input("Another card? Y/N")
          # we have a valid user input now
          # is it hit me or stay?
          if hitme in "Yy":
              playerhand.append(cards[startcard])
              startcard += 1  # or startcard = startcard + 1
              print(playerhand)
          else stop in"Nn":
              
