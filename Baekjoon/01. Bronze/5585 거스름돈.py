a = 1000 - int(input())
tmp = [500, 100, 50, 10, 5, 1]
count = 0
for i in tmp:
    count += a // i
    a %= i
print(count)