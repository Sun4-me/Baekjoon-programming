N, M = map(int, input().split())
tmp = []
res = []

for _ in range(N):
    tmp.append(input())

for a in range(N-7):
    for b in range(M-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if tmp[i][j] != 'W':
                        index1 += 1
                    if tmp[i][j] != 'B':
                        index2 += 1
                else:
                    if tmp[i][j] != 'B':
                        index1 += 1
                    if tmp[i][j] != 'W':
                        index2 += 1
        res.append(min(index1, index2))

print(min(res))