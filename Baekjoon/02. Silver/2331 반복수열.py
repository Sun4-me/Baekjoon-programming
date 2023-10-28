import sys

a, p = map(int, sys.stdin.readline().split())
data = [a]

while True:
    value = 0
    for i in str(data[-1]):
        value += int(i) ** p

    if value in data:
        break

    data.append(value)

print(data.index(value))
