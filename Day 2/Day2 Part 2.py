game = {}

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game = Whole Line
# Toss = One Section (divided by semicolon)
# Cube = Number plus color in format [num,color]

IDSum = 0

rMax = 12
gMax = 13
bMax = 14

with open("text.txt") as file:
    for game in file:
        ID = int(game.split(":")[0].split()[1])
        game = game.split(";")
        addID = True

        for toss in game:
            r = 0
            g = 0
            b = 0
            toss = toss.split(",")
            for cube in toss:
                cube = cube.strip().split(" ")
                match cube[1]:
                    case "red":
                        r += int(cube[0])
                    case "green":
                        g += int(cube[0])
                    case "blue":
                        b += int(cube[0])
            if r > rMax or b > bMax or g > gMax:
                addID = False
                break
        if addID:
            IDSum += ID

print(IDSum)