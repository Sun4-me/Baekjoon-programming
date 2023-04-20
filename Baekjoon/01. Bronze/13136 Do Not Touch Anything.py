R, C, N = map(int, input().split())
x = R // N + 1 if R % N else R // N
y = C // N + 1 if C % N else C // N
print(x * y)
