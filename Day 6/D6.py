with open(r"C:\Users\ctate0455\Desktop\Advent-of-Code-2023\Day 6\input.txt") as file:
    file = file.readlines()

times = file[0].split()[1:]
distance = file[1].split()[1:]

winAmount = 1

for i in range(len(times)):
    time = int(times[i])
    total = 0
    for holdTime in range(time):
        moveTime = time - holdTime
        distanceMoved = moveTime * holdTime
        if distanceMoved > int(distance[i]):
            total += 1
    winAmount *= total

print(winAmount)