import math

def quadratic(a,b,c):
    return (-b - math.sqrt(b*b-4*a*c)) / 2 * a

with open(r"C:\Users\ctate0455\Desktop\Advent-of-Code-2023\Day 6\input.txt") as file:
    file = file.readlines()

times = file[0].split()[1:]
distance = file[1].split()[1:]

winAmount = 1

for time, distance in zip(times, distance):
    n = int(time) + 1
    distance = int(distance)

    minIndex = math.floor(quadratic(1,-(n-1),distance))

    badTimes = 2 * (minIndex + 1)
    answer = n - badTimes

    print(f"Debug:\nN = {n}\nDistance = {distance}\nMin Index = {minIndex}\nBad Times = {badTimes}\nAnswer = {answer}\n")
    winAmount *= answer

print(winAmount)