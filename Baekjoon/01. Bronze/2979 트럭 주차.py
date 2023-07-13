a, b, c = map(int, input().split())
time = [0] * 100
sum = 0

for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        time[i] += 1

for j in time:
    if j == 0:
        sum += 0
    elif j == 1:
        sum += a
    elif j == 2:
        sum += b * 2
    elif j == 3:
        sum += c * 3

print(sum)
