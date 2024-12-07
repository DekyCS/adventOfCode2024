import math

f = open("./input/printing.txt", "r")

orderRule = []
updates = []

goodUpdates = []
badUpdates = []
middleCount = 0
middleCountFixed = 0

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

def check_order(update):
    for i in range(len(update)):
        if i == len(update) - 1:
            continue
        num_before = find_all_num_before(update[i])
        for j in range(len(update) - i - 1):
            if update[j + i + 1] in num_before:
                return i, j + i + 1
    return -1,-1 #usually -1 means it doesn't but in this code it does

def swap (a,b, arr):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

#Find the bad updates
for update in updates:
    result = check_order(update)
    if result != (-1,-1):
        badUpdates.append(update)
        swap(result[0], result[1], update)
        while True:
            result = check_order(update)
            if result == (-1,-1):
                break
            else:
                swap(result[0], result[1], update)

    elif result == (-1,-1):
        goodUpdates.append(update)

for goodUpdate in goodUpdates:
    middleCount += find_middle(goodUpdate)

for badUpdate in badUpdates:
    middleCountFixed += find_middle(badUpdate)

print(middleCountFixed)