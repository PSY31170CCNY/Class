#blackjack.py
from random import shuffle
#import random

# make a function that counts up the cards in a hand
def countup(hand):
	ace=False
total = 0

for card in range(len(hand)):
        #e.g hand[card] could be ('Queen', 'of', 'diamonds')
        # hand
        cardnum = hand[card][0]
if cardnum == "Ace":
            num = (1,11)
if cardnum in ("King","Queen","Jack","10"):
            num = 10
else:
    num = int(cardnum)
    total = total + num
if ace and total > 10:
	   total = total + 1
else:
    total = total + 11
    return 0 # -- return count of cards in a hand

#initialize variables
playerwins = 0
playerloses = 0
cards=[]
suits=["hearts","diamonds", "club","spades"]
numbers=["Ace","King","Queen","Jacks","10","9","8","7","6","5","4","3","2"]
for suit in range(len(suits)):
    for num in range(len(numbers)):
        cards.append((numbers[num]," of ",suits[suit]))
        # cards.append(numbers[num]+" of "+suits[suit])

shuffle(cards)

gameover = False #flag to tell us if no more cards in deck
startcard = 0
while not gameover:
      #check if the game is over: if there are fewer than 5 cards
     if startcard > 48:
        print("Game over! Player won", playerwins, "hands and lost ",playerloses)
        gameover = True
        break
    # starting a new hand
playerhand = cards[startcard:startcard+2]
startcard = startcard + 2 # or +=1
print("Here is your starting hand: ", playerhand)
    # what if the player gets 21 right away?
    # --> add up the cards!!
if countup(playerhand) == 21:
        # player wins automatically!!
    print("Congratulations, you win!")
        # check if game is over
        #for now, just continue the play loop
    playerwins +=1
    continue
    dealerhand = cards[startcard:startcard+2]
    startcard = startcard + 2 # or +=1
    hitme='x'
    while hitme not in ["YyNn"]:
        hitme = input("Another card? Y/N")
        # we have a valid user input now
        # is it hit me or stay?
        if hitme not in 'YyNn':
            print("enter Y or N, please")
            continue
        # give player another card
        if hitme in "Yy":
            playerhand.append(cards[startcard])
            startcard+=1 # or startcard = startcard + 1
            print(playerhand)
        # check the card totals
        # --> add up the cards!!
        total = countup(playerhand)
        if total > 21:
            #player loses
            print ("You lost.")
            playerloses +=1
            break
    if total == 21 :#playerwins
            print("Blackjack! You won!")
            Break
if total >= 21:
        gameover = False
        continue
 # No more cards dealt to player, see who won
playertot = count(playerhand)
dealertot = count(dealerhand)
if playertot > dealertot:
    print("Player wins with total count of",playercount)
else:
    print("Player loses with ",playercount," less than dealer's",dealercount) 
