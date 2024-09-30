path = r"C:\Users\Intern\Desktop\Advent-of-Code-2023\Day 7\input.txt"

with open(path) as file:
    file = {file.strip().split()[0]:file.strip().split()[1] for file in file.readlines()}

print(file)

def same(card:str):
    oldValue = card[0]
    for value in card:
        if oldValue != value:
            print("FAILED")
            return(False)
        oldValue = value
    print("PASSED")
    return(True)

five = []
four = []
full = []
three = []
twoPair = []
onePair = []
highCard = []

for card in file:
    same(card)