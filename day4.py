f =  open("xmas3.txt", "r")

xmas = []

theRest = "AS"
countOfXmas = 0

for x in f:
    temp = []
    for i in range(len(x)):
        temp.append(x[i])
    xmas.append(temp)

def isNotNegative(num):
    if num >= 0:
        return True
    return False

def checkTheRest(row, col, type):
    rowAdd = 0
    colAdd = 0
    match type:
        case "top":
            rowAdd = -1
        case "bottom":
            rowAdd = 1
        case "left":
            colAdd = -1
        case "right":
            colAdd = 1
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
    for index in range(len(theRest)): #theRest is "AS"
        if isNotNegative(row + (rowAdd * (index + 1))) and isNotNegative(col + (colAdd * (index + 1))):
            if xmas[row + (rowAdd * (index + 1))][col + (colAdd * (index + 1))] != theRest[index]:
                print("fails")
                return False
            print(f"Check for {index + 3} ({row + (rowAdd * (index + 1))},{col + (colAdd * (index + 1))}) = {theRest[index]} Verify: {xmas[row + (rowAdd * (index + 1))][col + (colAdd * (index + 1))]}")
    print("works")
    return True
for row in range(len(xmas)):
    try:
        for col in range(len(xmas[row])):
            if xmas[row][col] == "X":
                print(f"Check for 1 ({row},{col}) = X Verify: {xmas[row][col]}")
                #Check for "M" on top
                if isNotNegative(row-1):
                    if xmas[row-1][col] == "M":
                        print(f"Check for 2 ({row-1},{col}) = M Verify: {xmas[row-1][col]}")
                        if checkTheRest(row-1, col, "top"):
                            countOfXmas += 1
                # Check for "M" on bottom
                if xmas[row + 1][col] == "M":
                    print(f"Check for 2 ({row + 1},{col}) = M Verify: {xmas[row + 1][col]}")
                    if checkTheRest(row+1, col, "bottom"):
                        countOfXmas += 1
                # Check for "M" on left
                if isNotNegative(col-1):
                    if xmas[row][col-1] == "M":
                        print(f"Check for 2 ({row},{col - 1}) = M Verify: {xmas[row][col-1]}")
                        if checkTheRest(row, col-1, "left"):
                            countOfXmas += 1
                # Check for "M" on right
                if xmas[row][col + 1] == "M":
                    print(f"Check for 2 ({row},{col+1}) = M Verify: {xmas[row][col+1]}")
                    if checkTheRest(row, col+1, "right"):
                        countOfXmas += 1
                # Check for "M" on top left
                if isNotNegative(row-1) and isNotNegative(col-1):
                    if xmas[row - 1][col - 1] == "M":
                        print(f"Check for 2 ({row - 1},{col-1}) = M Verify: {xmas[row - 1][col-1]}")
                        if checkTheRest(row-1, col-1, "top left"):
                            countOfXmas += 1
                # Check for "M" on top right
                if isNotNegative(row-1):
                    if xmas[row - 1][col + 1] == "M":
                        print(f"Check for 2 ({row - 1},{col+1}) = M Verify: {xmas[row - 1][col+1]}")
                        if checkTheRest(row-1, col+1, "top right"):
                            countOfXmas += 1
                # Check for "M" on bottom left
                if isNotNegative(col - 1):
                    if xmas[row + 1][col - 1] == "M":
                        print(f"Check for 2 ({row + 1},{col-1}) = M Verify: {xmas[row+1][col-1]}")
                        if checkTheRest(row+1, col-1, "bottom left"):
                            countOfXmas += 1
                # Check for "M" on bottom right
                print(f"Check for 2 ({row+1},{col+1}) = M Verify: {xmas[row+1][col+1]}")
                if xmas[row + 1][col + 1] == "M":
                    if checkTheRest(row+1, col+1, "bottom right"):
                        countOfXmas += 1
    except:
        pass

print(countOfXmas)