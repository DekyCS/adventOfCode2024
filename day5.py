import math

f = open("./input/printing.txt", "r")

orderRule = []
updates = []

goodUpdates = []
middleCount = 0

for line in f:
    if "|" in line:
        x,y = line.split("|")
        orderRule.append((int(x),int(y)))
    elif "," in line:
        x = line.split(",")
        temp = []
        for y in x:
            temp.append(int(y))
        updates.append(temp)

def find_all_num_before(num):
    num_before = []
    for order in orderRule:
        if order[1] == num:
            num_before.append(order[0])
    return num_before

def find_middle(arr):
    return arr[math.floor(len(arr)/2)]


for update in updates:
    updateGood = True
    for i in range(len(update)):
        if i == len(update) - 1:
            continue
        num_before = find_all_num_before(update[i])
        for j in range(len(update) - i):
            if update[j + i] in num_before:
                updateGood = False
                break
        if not updateGood:
            break
    if updateGood:
        goodUpdates.append(update)

for goodUpdate in goodUpdates:
    middleCount += find_middle(goodUpdate)

print(middleCount)