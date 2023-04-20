import sys

n = int(sys.stdin.readline())
array = []


for i in range(n):
    [x, y] = list(map(int, sys.stdin.readline().split()))
    array.append([y, x])


array = sorted(array)

for i in range(n):
    print(array[i][1], array[i][0])
