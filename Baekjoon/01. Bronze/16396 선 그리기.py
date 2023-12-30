tmp = [0] * 10001
for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a, b):
        tmp[i] = 1
print(sum(tmp))
