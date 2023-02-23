N = int(input())
tmp = []

for _ in range(N):
    tmp.append(int(input()))

tmp = sorted(tmp)

for i in tmp:
    print(i)