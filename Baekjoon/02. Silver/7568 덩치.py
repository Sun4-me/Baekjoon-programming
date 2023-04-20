import sys

n = int(sys.stdin.readline())
array = []

for i in range(n):
    [x, y] = list(map(int, sys.stdin.readline().split()))
    array.append([x, y])

for i in array:
    rank = 1
    for j in array:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
