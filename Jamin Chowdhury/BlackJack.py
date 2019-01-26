#-----------Begin Game of BlackJack-------------------
from random import shuffle
cards = []
# Our lists that form the decks will be composed of two genres: suits and numbers
# There will be different combinations of suits and numbers
#---------------------------------------------------------------------
suits = ["♠","♥","♣","♦"]
#♠ = Spades
#♥ = Hearts
#♣ = Clubs
#♦ = Diamonds

#The 'suits' list shows the 4 classes of cards there are in a deck.

#--------------------------------------------------------------------------
numbers = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
#A = Ace ----> (Not that A or Ace can be worth 1 point or 11 points.)

#K = King
#Q = Queen
#J = Jack

#The 'numbers' list will show all the levels of cards within each class.
#------------------------------------------------------------------------

for suit in range(len(suits)):
    for num in range (len(numbers)):
        cards.append((numbers[num], 'of' , suits[suit],))
        
shuffle(cards)
#This will shuffle the cards such that the next draw is not in serial order.
#----------------------------------------------------------------------

gameover = True 
startcard = 0
#Make the program randomly automate one of the "cards"

while not gameover:
    playerhand = cards[startcard:startcard+2]
    startcard = starcard + 2
    print(playerhand)
    while hitme not in ["YyNn"]:
        hitme = input("Do you want another hit? Y/N")
    while hitme in "Yy":
        playerhand.append(cards[startcard])
#---------------------------------------------------------------------------
#The card combinations that equal to, or is closest to 21
#will win the game.
        




        
   
