#Python BlackJack Game
#import the random function to shuffle the deck 
import random

dealercards=[]

playercards=[]

#dealer cards
while len(dealercards) != 2:
    dealercards.append(random.randint(1,11))
    if len(dealercards)==2:
        print("Delear has x & ", dealercards[1])
        
#sum of the dealer's cards

if sum(dealercards)== 21:
    print("Dealer has 21 and wins")
elif sum(dealercards)>21:
    print("Dealer has busted!")


#player cards
while len(playercards) != 2:
    playercards.append(random.randint(1,11))
    if len(playercards)==2:
        print("You have ", playercards)        

# sum of the player's cards

while sum(playercards)<21:
    action=str(input("Do you want to stay or hit?(S/H)"))
    if action == "H":
        playercards.append(random.randint(1,11))
        print("You now have a totla of "+str(sum(playercards))+"from these cards", playercards)

    else:
        print("The dealer has a total of "+str(sum(dealercards))+"with", dealercards)
        print("You have a total of "+ str(sum(playercards))+ "with", playercards)
        if sum(dealercards)> sum(playercards):
            print("Dealer wins")
        else:
            print("You win!")
            break
if sum(playercards)>21:
    print("You busted and the dealer wins!")
elif sum(playercards)==21:
    print("You win!")
        
              
                    
