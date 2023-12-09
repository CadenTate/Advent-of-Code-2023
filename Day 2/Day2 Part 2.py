# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game = Whole Line
# Toss = One Section (divided by semicolon)
# Cube = Number plus color in format [num,color]

power = 0

with open(r"C:\Users\Caden\Desktop\Code\Advent-of-Code-2023\Day 2\inputDay2.txt") as file:
    for game in file:
        # Converting file to format used 
        game = game.split(":")
        game.pop(0)
        game = game[0].split(";")

        r = 0
        g = 0
        b = 0

        for toss in game:
            toss = toss.split(",")
            for cube in toss:
                cube = cube.strip().split(" ")
                cubeNum = int(cube[0])
                match cube[1]:
                    case "red":
                        if cubeNum > r:
                            r = cubeNum
                    case "green":
                        if cubeNum > g:
                            g = cubeNum
                    case "blue":
                        if cubeNum > b:
                            b = cubeNum
        power += r * g * b

print(power)