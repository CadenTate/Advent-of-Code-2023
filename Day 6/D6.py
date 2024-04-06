import math

def quadratic(a:int,b:int,c:int) -> float:
    return (-b - math.sqrt(b * b - 4*a*c)) / 2 * a

with open(r"C:\Users\Caden\Desktop\Code\Advent-of-Code-2023\Day 6\input.txt") as file:
    file = file.readlines()

times = file[0].split()[1:]
distances = file[1].split()[1:]

winAmount = 1

for time, distance in zip(times, distances):
    time = int(time)
    distance = int(distance)

    if time % 2 == 1: time += 1

    print(time, math.floor(quadratic(1,-time,distance)))

    winAmount *= math.ceil(time / 2) - quadratic(1,-time,distance) * 2

print(winAmount)