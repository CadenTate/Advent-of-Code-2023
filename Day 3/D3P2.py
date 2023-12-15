def isNum(num) -> bool:
    try:
        int(num)
        return True
    except:
        return False
    
def checkData(key:int,isDataNum:bool=False) -> None:
    if isDataNum:
        if key not in dataNums:
            dataNums[key] = []
    else: 
        if key not in data:
            data[key] = 0

# Get File Setup
prefix = r"C:\Users\ctate0455\Desktop\Code\Advent-of-Code-2023\Day 3"
filename = "inputDay3.txt"

# Get File
with open(prefix + "\\" + filename) as file:
    file = file.readlines()

# Validate Schematic
if len(file[0]) -1 != len(file):
    raise Exception("FIle NOT FOUND")

length = len(file)

# Preparing File
text = ""

for line in file:
    text += line.strip()

# Logic
num = ""
data = {}
dataNums = {}

# Iterate Through Each Character
for i,char in enumerate(text):
    if isNum(char): 
        num += char
    else:
        # Do stuff if the number has no more digits
        if num != "":
            for f,digit in enumerate(num):
                # Check up and down first since all digits of num need to do that

                # Up
                digitIndex = i-len(num)-length+f
                if digitIndex > 0 and text[digitIndex] == "*":
                    checkData(digitIndex)
                    data[digitIndex] += 1
                    checkData(digitIndex,True)
                    dataNums[digitIndex].append(num) 
                    print("NUM:",num,"DIGIT:",digit,"UP")
                    break

                # Down
                digitIndex = i - len(num) + length + f
                if digitIndex < len(text) and text[digitIndex] == "*":
                    checkData(digitIndex)
                    data[digitIndex] += 1
                    checkData(digitIndex,True)
                    dataNums[digitIndex].append(num) 
                    print("NUM:",num,"DIGIT:",digit,"down")
                    break

                # Check 45 degrees
                # Up Left
                digitIndex = i - len(num) + f - length + 1
                if  digitIndex > 0 and text[digitIndex] == "*":
                    checkData(digitIndex)
                    data[digitIndex] += 1
                    checkData(digitIndex,True)
                    dataNums[digitIndex].append(num) 
                    print("NUM:",num,"DIGIT:",digit,"UP left")
                    break
                # Down Left
                digitIndex = i - len(num) + length - 1 + f
                if digitIndex < len(text) and text[digitIndex] == "*":
                    checkData(digitIndex)
                    data[digitIndex] += 1
                    checkData(digitIndex,True)
                    dataNums[digitIndex].append(num) 
                    print("NUM:",num,"DIGIT:",digit,"Dwon Left")
                    break
                # Up Right
                digitIndex = i -len(num) - length - 1 + f
                if digitIndex > 0 and text[digitIndex] == "*":
                    checkData(digitIndex)
                    data[digitIndex] += 1
                    checkData(digitIndex,True)
                    dataNums[digitIndex].append(num) 
                    print("NUM:",num,"DIGIT:",digit,"UP Right")
                    break
                # Down Right
                digitIndex = i - len(num) + length + 1 + f
                if digitIndex < len(text) and text[digitIndex] == "*":
                    checkData(digitIndex)
                    data[digitIndex] += 1
                    checkData(digitIndex,True)
                    dataNums[digitIndex].append(num)
                    print("NUM:",num,"DIGIT:",digit,"Down Right")
                    break

            # Unique Cases for first and last
            # First Digit Case
            digitIndex = i - len(num) - 1 
            if digitIndex > -1 and text[digitIndex] == "*":
                checkData(digitIndex)
                data[digitIndex] += 1
                checkData(digitIndex,True)
                dataNums[digitIndex].append(num) 
                print("NUM:",num,"DIGIT:",num[0],"Left")
                # Last Digit
            digitIndex = i
            if text[digitIndex] == "*":
                checkData(digitIndex)
                data[digitIndex] += 1
                checkData(digitIndex,True)
                dataNums[digitIndex].append(num) 
                print("NUM:",num,"DIGIT:",num[-1],"Right")

        # Reset num
        num = ""  

sum = 0

for cog in data:
    if data[cog] == 2:
        sum += int(dataNums[cog][0]) * int(dataNums[cog][1]) 

print(sum)