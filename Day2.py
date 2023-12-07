game = {}

with open("test.txt") as file:
    line = str.split(file.readline(),",")
    line = [i.split(",") for i in line]
    print(line)