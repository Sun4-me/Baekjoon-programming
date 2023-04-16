a, b = map(int, input().split())

tmp = []
for i in range(1 , b+1):
    for _ in range(i):
        tmp.append(i)

print(sum(tmp[a-1:b]))