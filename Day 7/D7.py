path = r"C:\Users\ctate0455\Desktop\Advent-of-Code-2023\Day 7\input.txt"

with open(path) as file:
    file = file.readlines()

file = [item.split() for item in file]

score = {}

for item in file:
    card = {}
    for letter in item[0]:
        if letter not in card:
            card[letter] = 1
        else:
            card[letter] += 1
    
    values = [value for value in card.values()]

    print(values)

    if 5 in values:
        score[item[1]] = 7
    elif 4 in values:
        score[item[1]] = 6
    elif 3 in values and 2 in values:
        score[item[1]] = 5
    elif values.count(3) == 1 and values.count(1) == 2:
        score[item[1]] = 4
    elif values.count(1) == 2 or values.count(2) == 2:
        score[item[1]] = 3
    elif 2 in values:
        score[item[1]] = 2
    else:
        score[item[1]] = 1
        
print(score)