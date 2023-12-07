sum = 0

validNumbers = ("one", "two", "three", "four", "five", "six", "seven", "eight","nine")

def checkInt(num) -> bool:
    try:
        int(num)
        return True
    except:
        return False


# Open File
with open("test.txt") as text:
    # Iterate through every line
    for line in text:
        firstNum = -1
        lastNum = -1
        # Find first number
        for char in line:
            if checkInt(char):
                firstNum = int(char)
                break


        # Find second number
        for char in reversed(line):
            if checkInt(char):
                lastNum = int(char)
                break
            else:
                lastNum = -1


        # Setup for finding string numbers
        firstindex = len(line)
        lastindex = -1
        firstWord = ""
        lastWord = ""


        # Find string numbers
        for num in validNumbers:
            # First Number
            if -1 < line.find(num) < firstindex:
                firstindex = line.find(num)
                firstWord = num
            # Last Number
            if line.rfind(num) > lastindex:
                lastindex = line.rfind(num)
                lastWord = num


        if line.index(str(firstNum)) < firstindex:
            finalFirst = firstNum
        else:
            finalFirst = validNumbers.index(firstWord) + 1


        if line.rindex(str(lastNum)) > lastindex:
            finalLast = lastNum
        else:
            finalLast = lastWord


        print(finalFirst,finalLast)



