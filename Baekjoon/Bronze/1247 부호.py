from sys import stdin

for _ in range(3):
    N = int(stdin.readline())
    tmp = [int(stdin.readline()) for i in range(N)]
    if sum(tmp) == 0:
        print("0")
    elif sum(tmp) > 0:
        print("+")
    else:
        print("-")