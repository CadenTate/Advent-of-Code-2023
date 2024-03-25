import math

def quadratic(a,b,c):
    return ((-b - math.sqrt(b*b-4*a*c)) / 2 * a,(-b + math.sqrt(b*b-4*a*c)) / 2 * a)

with open(r"C:\Users\ctate0455\Desktop\Advent-of-Code-2023\Day 6\input.txt") as file:
    file = file.readlines()

times = file[0].split()[1:]
distance = file[1].split()[1:]

winAmount = 1

for time, distance in zip(times, distance):
    n = int(time)
    distance = int(distance)

    answer = quadratic(1,-n,distance)
    answer = answer[1] - answer[0]

    print(f"Debug:\nN = {n}\nDistance = {distance}\nAnswer = {answer}\n")
    winAmount *= math.floor(answer)

print(winAmount)
