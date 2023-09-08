import sys

input = sys.stdin.readline

tmp = []
for _ in range(int(input())):
    s = input().rstrip()

    summ = 0
    for i in s:
        if i.isdigit():
            summ += int(i)
    tmp.append((s, summ))

tmp.sort(key=lambda x: (len(x[0]), x[1], x[0]))

for i in tmp:
    print(i[0])
