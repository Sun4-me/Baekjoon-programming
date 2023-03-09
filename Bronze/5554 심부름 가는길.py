tmp = []

for _ in range(4):
    tmp.append(int(input()))

sum_time=sum(tmp)

x = sum_time // 60
y = sum_time % 60

print(x)
print(y)