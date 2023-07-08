n, m, l = map(int, input().split())
game = [0] * n
cnt = 0
start = 0
while game[0] != m:
    game[start] += 1
    start = (start + l) % n
    cnt += 1
print(cnt - 1)
