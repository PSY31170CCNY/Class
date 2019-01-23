from random import shuffle

def countup(hand):
    ace = False
    total = 0
    for card in range(len(hand)):
        cardnum = hand[card][0]
        if cardnum == "ace" :
            num = 0
            ace = true
        if cardnum in ('king','queen','jack','10'):
            num = 10
        else:
            num = int(cardnum)
        total = total + num
        if ace and (card == len(hand)-1):
            total
        if ace and total > 10
            total = total + 1
            else 
    return 0

playerwins = 0
playerloses = 0
cards=[]
numbers = [ 'ace','2','3','4','5','6','7','8','9','10''jack','queen','king' ]
suits = [ 'clubs','spades','hearts','diamonds' ]
for x in range(len(suits)):
    for num in range(len(numbers)):
        cards.append((numbers[num], "of" , suits[x]))
        
shuffle(cards)

gameover = false
startcard = 0
while not gameover:
    if startcard > 48:
        print("game over, player wins")
    playerhand = cards[startcard:startcard+2]
    startcard = startcard + 2 # or +=1
    print(" Here is your starting hand: ", playerhand)
    if countup(playerhand) == 21:
        print("congratulations, you win!")
        playerwins +=1
        continue
    hitme='x'
    while hitme not in ["YyNn"]:
        hitme = input("another card? Y/N")
        if hitme not in 'YyNn'
            print('enter Y or N please')
            continue
        if hitme in "Yy":
            playerhand.append(cards[startcard])
            startcard +=1 # or startcard = startcard + 1
            print(playerhand)
            total = countup(cards)
            if total > 21 :
                print("you lost")
                playerloses +=1
                break
            if total == 21 :
                print('you win")
                playerwins +=1
                break
    if total >= 21 :
        gameover = False
        continue
    playertot = count(playerhand)
    dealertot = count(dealerhand)
    if playertot > dealertot:
        print("player wins with total count of", playercount , "greater than dealer's", dealercount)
