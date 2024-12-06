from numpy.linalg.linalg import solve

f =  open("xmas.txt", "r")

xmas = []
mDoNotUse = []

theRest = "AS"
countOfXmas = 0

for x in f:
    temp = []
    for i in range(len(x)):
        temp.append(x[i])
    xmas.append(temp)

def isInRange(row,col):
    if row < 0 or row >= len(xmas):
        return False
    if col < 0 or col >= len(xmas[row]):
        return False
    return True

def checkTheRest(row, col, type):
    rowAdd = 0
    colAdd = 0
    match type:
        case "top left":
            rowAdd = -1
            colAdd = -1
        case "top right":
            rowAdd = -1
            colAdd = 1
        case "bottom left":
            rowAdd = 1
            colAdd = -1
        case "bottom right":
            rowAdd = 1
            colAdd = 1
        case _:
            print(type)
            return False
    if isInRange(row + (rowAdd * 1), col + (colAdd * 1)):
        if xmas[row + (rowAdd * 1)][col + (colAdd * 1)] != "S":
            print("fails")
            return False
        print(f"Check for {3} ({row + (rowAdd * 1)},{col + (colAdd * 1)}) = S Verify: {xmas[row + (rowAdd * 1)][col + (colAdd * 1)]}")
    else:
        print("fails")
        return False
    #print("works")
    return True

def findMAS(row,col):
    countThatWorks = 0
    try:
        print(f"({row},{col})")
        if xmas[row][col] == "M":
            print(f"Check for 1 ({row},{col}) = M Verify: {xmas[row][col]}")
            # Check for "A" on top left
            print("Check top left")
            if isInRange(row - 1, col - 1):
                if xmas[row - 1][col - 1] == "A":
                    print(f"Check for 2 ({row - 1},{col - 1}) = A Verify: {xmas[row - 1][col - 1]}")
                    if checkTheRest(row - 1, col - 1, "top left"):
                        #Check the whole x
                        if isInRange(row-2,col) and isInRange(row, col-2):
                            if xmas[row-2][col] == "M":
                                if xmas[row][col-2] == "S":
                                    countThatWorks+=1
                            elif xmas[row-2][col] == "S":
                                if xmas[row][col-2] == "M":
                                    countThatWorks+=1
            # Check for "M" on top right
            print("Check top right")
            if isInRange(row - 1, col + 1):
                if xmas[row - 1][col + 1] == "A":
                    print(f"Check for 2 ({row - 1},{col + 1}) = A Verify: {xmas[row - 1][col + 1]}")
                    if checkTheRest(row - 1, col + 1, "top right"):
                        # Check the whole x
                        if isInRange(row - 2, col) and isInRange(row, col + 2):
                            if xmas[row - 2][col] == "M":
                                if xmas[row][col + 2] == "S":
                                    countThatWorks += 1
                            elif xmas[row - 2][col] == "S":
                                if xmas[row][col + 2] == "M":
                                    countThatWorks += 1
            # Check for "M" on bottom left
            print("Check bottom left")
            if isInRange(row + 1, col - 1):
                if xmas[row + 1][col - 1] == "A":
                    print(f"Check for 2 ({row + 1},{col - 1}) = A Verify: {xmas[row + 1][col - 1]}")
                    if checkTheRest(row + 1, col - 1, "bottom left"):
                        # Check the whole x
                        if isInRange(row + 2, col) and isInRange(row, col - 2):
                            if xmas[row + 2][col] == "M":
                                if xmas[row][col - 2] == "S":
                                    countThatWorks += 1
                            elif xmas[row + 2][col] == "S":
                                if xmas[row][col - 2] == "M":
                                    countThatWorks += 1
            # Check for "M" on bottom right
            print("Check bottom right")
            if isInRange(row + 1, col + 1):
                if xmas[row + 1][col + 1] == "A":
                    print(f"Check for 2 ({row + 1},{col + 1}) = A Verify: {xmas[row + 1][col + 1]}")
                    if checkTheRest(row + 1, col + 1, "bottom right"):
                        # Check the whole x
                        if isInRange(row + 2, col) and isInRange(row, col + 2):
                            if xmas[row + 2][col] == "M":
                                if xmas[row][col + 2] == "S":
                                    countThatWorks += 1
                            elif xmas[row + 2][col] == "S":
                                if xmas[row][col + 2] == "M":
                                    countThatWorks += 1
        if countThatWorks > 0:
            mDoNotUse.append((row,col))
        return countThatWorks
    except Exception as error:
        print(f"Error: ({row},{col}) || {error}")
        pass

for row in range(len(xmas)):
    for col in range(len(xmas[row])):
        countOfXmas += findMAS(row,col)


print(countOfXmas)
print(countOfXmas/2)


