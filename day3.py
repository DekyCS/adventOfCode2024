mul = "mul()"


maxSearchLength = 8

finalSum = 0

input = ""

f = open("multiply.txt", "r")
for x in f:
  input += x

doI = True

for char in range(len(input)):
    try:
        if input[char] == "d":
            if input[char + 1] == "o":
                if input[char + 2] == "(":
                    if input[char + 3] == ")":
                        doI = True
                elif input[char + 2] == "n":
                    if input[char + 3] == "'":
                        if input[char + 4] == "t":
                            if input[char + 5] == "(":
                                if input[char + 6] == ")":
                                    doI = False
        if doI:
            if input[char] == "m":
                if input[char + 1] == "u":
                    if input[char + 2] == "l":
                        if input[char + 3] == "(":
                            searchGood = False
                            for i in range(maxSearchLength):
                                if input[char + 4 + i] == ")":
                                    parameters = ""
                                    for j in range(i):
                                        parameters += input[char + 4 + j]
                                    if len(parameters) < 3:
                                        break
                                    x, y = parameters.split(",")
                                    searchGood = True
                                    finalSum += (int(x)*int(y))
                                    searchGood = True
                                    break
    except:
        continue

print(finalSum)