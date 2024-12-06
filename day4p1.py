f =  open("input/xmas.txt", "r")

xmas = []

theRest = "AS"
countOfXmas = 0

for x in f:
    temp = []
    for i in range(len(x)):
        temp.append(x[i])
    xmas.append(temp)

def isInRange(row,col):
    print(f"Hello: ({row},{col})")
    if row < 0 or row >= len(xmas):
        return False
    if col < 0 or col >= len(xmas[row]):
        print("was not working")
        return False
    return True

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
        if isInRange(row + (rowAdd * (index + 1)), col + (colAdd * (index + 1))):
            if xmas[row + (rowAdd * (index + 1))][col + (colAdd * (index + 1))] != theRest[index]:
                print("fails")
                return False
            print(f"Check for {index + 3} ({row + (rowAdd * (index + 1))},{col + (colAdd * (index + 1))}) = {theRest[index]} Verify: {xmas[row + (rowAdd * (index + 1))][col + (colAdd * (index + 1))]}")
        else:
            print("fails")
            return False
    print("works")
    return True
for row in range(len(xmas)):
    for col in range(len(xmas[row])):
        try:
            print(f"({row},{col})")
            if xmas[row][col] == "M":
                print(f"Check for 1 ({row},{col}) = M Verify: {xmas[row][col]}")
                #Check for "M" on top
                print("Check top")
                if isInRange(row - 1, col):
                    if xmas[row-1][col] == "M":
                        print(f"Check for 2 ({row-1},{col}) = M Verify: {xmas[row-1][col]}")
                        if checkTheRest(row-1, col, "top"):
                            countOfXmas += 1
                # Check for "M" on bottom
                print("Check bottom")
                if isInRange(row+1, col):
                    if xmas[row + 1][col] == "M":
                        print(f"Check for 2 ({row + 1},{col}) = M Verify: {xmas[row + 1][col]}")
                        if checkTheRest(row+1, col, "bottom"):
                            countOfXmas += 1
                # Check for "M" on left
                print("Check left")
                if isInRange(row, col - 1):
                    if xmas[row][col-1] == "M":
                        print(f"Check for 2 ({row},{col - 1}) = M Verify: {xmas[row][col-1]}")
                        if checkTheRest(row, col-1, "left"):
                            countOfXmas += 1
                # Check for "M" on right
                print(f"Check right ({row},{col+1})")
                if isInRange(row, col+1):
                    print(f"({row},{col}) is in range")
                    if xmas[row][col + 1] == "M":
                        print(f"Check for 2 ({row},{col+1}) = M Verify: {xmas[row][col+1]}")
                        if checkTheRest(row, col+1, "right"):
                            countOfXmas += 1
                # Check for "M" on top left
                print("Check top left")
                if isInRange(row - 1, col-1):
                    if xmas[row - 1][col - 1] == "M":
                        print(f"Check for 2 ({row - 1},{col-1}) = M Verify: {xmas[row - 1][col-1]}")
                        if checkTheRest(row-1, col-1, "top left"):
                            countOfXmas += 1
                # Check for "M" on top right
                print("Check top right")
                if isInRange(row - 1, col+1):
                    if xmas[row - 1][col + 1] == "M":
                        print(f"Check for 2 ({row - 1},{col+1}) = M Verify: {xmas[row - 1][col+1]}")
                        if checkTheRest(row-1, col+1, "top right"):
                            countOfXmas += 1
                # Check for "M" on bottom left
                print("Check bottom left")
                if isInRange(row+1,col - 1):
                    if xmas[row + 1][col - 1] == "M":
                        print(f"Check for 2 ({row + 1},{col-1}) = M Verify: {xmas[row+1][col-1]}")
                        if checkTheRest(row+1, col-1, "bottom left"):
                            countOfXmas += 1
                # Check for "M" on bottom right
                print("Check bottom right")
                if isInRange(row+1, col+1):
                    if xmas[row + 1][col + 1] == "M":
                        print(f"Check for 2 ({row + 1},{col + 1}) = M Verify: {xmas[row + 1][col + 1]}")
                        if checkTheRest(row+1, col+1, "bottom right"):
                            countOfXmas += 1
        except Exception as error:
            print(f"Error: ({row},{col}) || {error}")
            pass

print(countOfXmas)
