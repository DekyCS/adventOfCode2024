import os

leftSide = []
rightSide = []
similarityScore = 0

f = open("input.txt", "r")
for x in f:
  left, right = x.split("   ")
  leftSide.append(int(left))
  rightSide.append(int(right))

leftSide.sort()
rightSide.sort()

for i in range(len(leftSide)):
    count = 0
    for j in range(len(rightSide)):
        if (leftSide[i] == rightSide[j]):
            count += 1
    similarityScore += (count * leftSide[i])

print(similarityScore)