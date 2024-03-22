# Opening and Preparing File
path = r"C:\Users\Caden\Desktop\Code\Advent-of-Code-2023\Day 5"
filename = "inputDay5.txt"

file = open(path+"\\"+filename)
text = file.readlines()
file.close()

text = [line.strip() for line in text]

# Get Seeds
seedsRange = text.pop(0).split(":")[1].strip().split()
seedsRange = [int(seed) for seed in seedsRange]
del text[0]

# Initialize Keys
keys = {"s2s":[],"s2f":[],"f2w":[],"w2l":[],"l2t":[],"t2h":[],"h2l":[]}
keysList = list(keys)

saveLocation = 0

for line in text:
    if line == "":
        saveLocation += 1
    
    line = line.split()
    if len(line) == 3:
        line = [int(num) for num in line]
        keys[keysList[saveLocation]].append(line)

# Proccessing Logic
min = -1

for i in range(1,len(seedsRange),2):
    for f in range(seedsRange[i]):
        value = seedsRange[i-1]+f
        for key in keysList:
            maps = keys[key]
            for map in maps:
                if map[1] <= value < map[1] + map[2]:
                    value = map[0] + (value - map[1])
                    break
        if value < min or min == -1: min = value

print(min)