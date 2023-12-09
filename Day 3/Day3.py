def isNum(num) -> bool:
    try:
        int(num)
        return True
    except:
        return False

# Get File Setup
prefix = r"C:\Users\Caden\Desktop\Code\Advent-of-Code-2023\Day 3"
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
sum = 0
num = ""

# Iterate Through Each Character
for i,char in enumerate(text):
    if isNum(char): 
        num += char
    else:
        # Do stuff if the number has no more digits
        if num != "":
            for f,digit in enumerate(num):
                # Check up and down first since all digits of num need to do that
                if i - len(num) - length + f > 0 and text[i-len(num)-length+f] != ".":
                    sum += int(num)
                    print("NUM:",num,"DIGIT:",digit,"UP")
                    break
                if i - len(num) + length + f < len(text) and text[i-len(num)+length+f] != ".":
                    sum += int(num)
                    print("NUM:",num,"DIGIT:",digit,"down")
                    break

                # Check 45 degrees
                # Up Left
                if i - len(num) + f - length + 1 > 0 and text[i-len(num)+f-length + 1] != ".":
                    sum += int(num)
                    print("NUM:",num,"DIGIT:",digit,"UP left")
                    break
                # Down Left
                if i - len(num) + length - 1 + f < len(text) and text[i-len(num)+length - 1+f] != ".":
                    sum += int(num)
                    print("NUM:",num,"DIGIT:",digit,"Dwon Left")
                    break
                # Up Right
                if i - len(num) - length - 1 + f > 0 and text[i-len(num)-length - 1+f] != ".":
                    sum += int(num)
                    print("NUM:",num,"DIGIT:",digit,"UP Right")
                    break
                # Down Right
                if i - len(num) + length + 1 + f < len(text) and text[i-len(num)+length + 1+f] != ".":
                    sum += int(num)
                    print("NUM:",num,"DIGIT:",digit,"Down Right")
                    break

            # Unique Cases for first and last
            # First Digit Case
            if i - len(num) - 1 > -1 and text[i - len(num) - 1] != ".":
                sum += int(num)
                print("NUM:",num,"DIGIT:",num[0],"Left")
                # Last Digit
            if text[i] != ".":
                print("NUM:",num,"DIGIT:",num[-1],"Right")
                sum += int(num)

        # Reset num
        num = ""  

print(sum)