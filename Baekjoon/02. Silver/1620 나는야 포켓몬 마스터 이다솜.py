import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}

for i in range(1, n + 1):
    tmp = input().rstrip()
    dict[i] = tmp
    dict[tmp] = i

for i in range(m):
    tmp = input().rstrip()
    if tmp.isdigit():
        print(dict[int(tmp)])
    else:
        print(dict[tmp])
