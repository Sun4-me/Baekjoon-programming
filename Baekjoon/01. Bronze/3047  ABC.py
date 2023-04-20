import sys

input = sys.stdin.readline

num = list(map(int, input().split()))
num = sorted(num)

index = input()
for i in index:
    if i == "A":
        print(num[0], end=" ")
    elif i == "B":
        print(num[1], end=" ")
    elif i == "C":
        print(num[2], end=" ")
