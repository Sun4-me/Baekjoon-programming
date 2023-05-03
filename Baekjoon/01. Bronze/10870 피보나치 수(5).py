d = [0, 1, 1]

n = int(input())

for i in range(3, n + 1):
    num = d[i - 1] + d[i - 2]
    d.append(num)


print(d[n])
