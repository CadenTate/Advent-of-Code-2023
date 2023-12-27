path = r"C:\Users\Caden\Desktop\Code\Advent-of-Code-2023\Day 4"
filename = "inputDay4.txt"

file = open(path+"\\"+filename,"r")

lines = file.readlines()

file.close()

loopAmount = 0

def cardLooper(cardNum:int,card:list):
    global loopAmount
    loopAmount += 1
    winSum = 0
    for num in card[0]:
        if num in card[1]:
            winSum += 1
    
    for i in range(winSum):
        cardLooper(i+1+cardNum,startCards[i+1+cardNum])

# Reference Card / First Card
startCards = {}

for card in lines:
    cardNum = int(card.split(":")[0][5:])
    cardPoints = card.split(":")[1].strip().split("|")

    cardPoints = [i.split() for i in cardPoints]

    startCards[cardNum] = cardPoints

# Loop Algorithm
for cardNum in startCards:
    cardLooper(cardNum,startCards[cardNum])

print(loopAmount)