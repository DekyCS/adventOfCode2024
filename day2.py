safeReport = 0
reports = []

f = open("reports.txt", "r")
for x in f:
  reports.append(x.split(" "))

def isItSafe(input):
    isIncreasing = True
    before = 0
    current = 0
    for i in range(len(input)):
        current = int(input[i])
        if (i == 0):
            before = current
            continue
        elif (i == 1):
            if (current < before):
                isIncreasing = False
        else:
            if ((current < before and isIncreasing) or (current > before and isIncreasing == False)):
                return False

        if ((abs(before - current) > 3) or (before == current)):
            return False

        before = current
    return True

def copyArray(input):
    newArr = []
    for num in input:
        newArr.append(num)
    return newArr


for x in reports:
    if (isItSafe(x)):
        safeReport += 1
    else:
        for i in range(len(x)):
            newArr = copyArray(x)
            newArr.pop(i)
            if (isItSafe(newArr)):
                safeReport+= 1
                break
print(safeReport)

