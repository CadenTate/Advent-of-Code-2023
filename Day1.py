sum = 0

validNumbers = ("one", "two", "three", "four", "five", "six", "seven", "eight","nine")

# Open File
with open("test.txt") as text:
    # Iterate through every line
    # for i in text:
    #     # iterate through each character
    #     for f in i:
    #         try:
    #             f = int(f)
    #             sum += f * 10
    #             print(f)
    #             break
    #         except:
    #             continue 
    #     for f in reversed(i):
    #         try:
    #             f = int(f)
    #             sum += f
    #             print(f)
    #             break
    #         except:
    #             continue

    for line in text:
        for char in range(len(line)):
            if line[i]

# print(sum)