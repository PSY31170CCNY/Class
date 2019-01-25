#Final Assignment #2

>>> suits=["hearts","diamonds", "club","spades"]

>>> numbers=["Ace","King","Queen","Jacks","10","9","8","7","6","5","4","3","2"]

>>> len(suits)

4

>>> len(numbers)

13

>>> range(len(suits))

range(0, 4)

>>>

__________________________________________________________

suits=["hearts","diamonds", "club","spades"]

numbers=["Ace","King","Queen","Jacks","10","9","8","7","6","5","4","3","2"]

for x in range(len(suits)):

print(suits[x])

Python:

hearts

diamonds

club

spades

__________________________________________________________

suits=["hearts","diamonds", "club","spades"]

numbers=["Ace","King","Queen","Jacks","10","9","8","7","6","5","4","3","2"]

for suit in range(len(suits)):

for num in range(len(numbers)):

print(suits[suit],numbers[num])

Python:

hearts Ace

hearts King

hearts Queen

hearts Jacks

hearts 10

hearts 9

hearts 8

hearts 7

hearts 6

hearts 5

hearts 4

hearts 3

hearts 2

diamonds Ace

diamonds King

diamonds Queen

diamonds Jacks

diamonds 10

diamonds 9

diamonds 8

diamonds 7

diamonds 6

diamonds 5

……..

Add print(numbers[num],"of",suits[suit]) for this - Jacks of spades

___________________________________________________________________

cards=[ ]

suits=["hearts","diamonds", "club","spades"]

numbers=["Ace","King","Queen","Jacks","10","9","8","7","6","5","4","3","2"]

for suit in range(len(suits)):

for num in range(len(numbers)):

cards.append((numbers[num]," of ", suits[suit]))

Python:

>>> cards

[('Ace', ' of ', 'hearts'), ('King', ' of ', 'hearts'), ('Queen', ' of ', 'hearts'), ('Jacks', ' of ', 'hearts'), ('10', ' of ', 'hearts'), ('9', ' of ', 'hearts'), ('8', ' of ', 'hearts'), ('7', ' of ', 'hearts'), ('6', ' of ', 'hearts'), ('5', ' of ', 'hearts'), ('4', ' of ', 'hearts'), ('3', ' of ', 'hearts'), ('2', ' of ', 'hearts'), ('Ace', ' of ', 'diamonds'), ('King', ' of ', 'diamonds'), ('Queen', ' of ', 'diamonds'), ('Jacks', ' of ', 'diamonds'), ('10', ' of ', 'diamonds'), ('9', ' of ', 'diamonds'), ('8', ' of ', 'diamonds'), ('7', ' of ', 'diamonds'), ('6', ' of ', 'diamonds'), ('5', ' of ', 'diamonds'), ('4', ' of ', 'diamonds'), ('3', ' of ', 'diamonds'), ('2', ' of ', 'diamonds'), ('Ace', ' of ', 'club'), ('King', ' of ', 'club'), ('Queen', ' of ', 'club'), ('Jacks', ' of ', 'club'), ('10', ' of ', 'club'), ('9', ' of ', 'club'), ('8', ' of ', 'club'), ('7', ' of ', 'club'), ('6', ' of ', 'club'), ('5', ' of ', 'club'), ('4', ' of ', 'club'), ('3', ' of ', 'club'), ('2', ' of ', 'club'), ('Ace', ' of ', 'spades'), ('King', ' of ', 'spades'), ('Queen', ' of ', 'spades'), ('Jacks', ' of ', 'spades'), ('10', ' of ', 'spades'), ('9', ' of ', 'spades'), ('8', ' of ', 'spades'), ('7', ' of ', 'spades'), ('6', ' of ', 'spades'), ('5', ' of ', 'spades'), ('4', ' of ', 'spades'), ('3', ' of ', 'spades'), ('2', ' of ', 'spades')]

____________________________________________________________________

from random import shuffle

cards=[]

suits=["hearts","diamonds", "club","spades"]

numbers=["Ace","King","Queen","Jacks","10","9","8","7","6","5","4","3","2"]

for suit in range(len(suits)):

for num in range(len(numbers)):

cards.append((numbers[num]," of ", suits[suit]))

shuffle(cards)

print(cards)

Python:

Shuffles list

____________________________________________________________________

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

# -- return count of cards in a hand

return 0

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
