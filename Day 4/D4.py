path = r"C:\Users\Caden\Desktop\Code\Advent-of-Code-2023\Day 4"
filename = "inputDay4.txt"

with open(path+"\\"+filename) as file:
    sum = 0

    file = [line.split("|") for line in file.readlines()]

    winNums = [card.split(":")[1].strip().split() for card in [line[0] for line in file]]
    haveNums = [card.strip().split() for card in [line[1] for line in file]]

    for i,card in enumerate(haveNums):
        cardSum = 0
        for num in card:
            if num in winNums[i]:
                print(i,num)
                if cardSum == 0:
                    cardSum = 1
                else:
                    cardSum *= 2
        sum += cardSum

print(sum)