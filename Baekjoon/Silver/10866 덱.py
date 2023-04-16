from collections import deque
import sys

d = deque()
n = int(input())

for i in range(n):
    A = sys.stdin.readline().split()

    if A[0] == "push_front":
        d.appendleft(A[1])
    elif A[0] == "push_back":
        d.append(A[1])
    elif A[0] == "pop_front":
        if d:
            print(d[0])
            d.popleft()
        else:
            print(-1)
    elif A[0] == "pop_back":
        if d:
            print(d[-1])
            d.pop()
        else:
            print(-1)
    elif A[0] == "size":
        print(len(d))
    elif A[0] == "empty":
        if d:
            print(0)
        else:
            print(1)
    elif A[0] == "front":
        if d:
            print(d[0])
        else:
            print(-1)
    elif A[0] == "back":
        if d:
            print(d[-1])
        else:
            print(-1)
