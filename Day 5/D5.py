# Opening and Preparing File
path = r"C:\Users\Caden\Desktop\Code\Advent-of-Code-2023\Day 5"
filename = "inputDay5.txt"

file = open(path+"\\"+filename)
text = file.readlines()
file.close()

text = [line.strip() for line in text]

# Get Seeds
seeds = text.pop(0).split(":")[1].strip().split()
seeds = [int(seed) for seed in seeds]
del text[0]

# Initialize Keys
keys = {"s2s":{},"s2f":{},"f2w":{},"w2l":{},"l2t":{},"t2h":{},"h2l":{}}
keysList = list(keys)

saveLocation = 0

for line in text:
    if line == "":
        saveLocation += 1

    line = line.split()

    if len(line) == 3 or line == "":
        line = [int(num) for num in line]
        destination = [line[0] + i for i in range(line[2])]
        source = [line[1] + i for i in range(line[2])]

        for i in range(len(source)):
            keys[keysList[saveLocation]][source[i]] = destination[i]
print("Keys Processed")

# Seed Convertion Logic
min = -1

for seed in seeds:
    value = seed
    for key in keysList:
        try:
            value = keys[key][value]
        except KeyError as e:
            continue
    if value < min or min == -1: min = value
print(min)