import sys

a, b = map(int, sys.stdin.readline().split())
if a > b:
    a, b = b, a
print(b * (b + 1) // 2 - a * (a - 1) // 2)
