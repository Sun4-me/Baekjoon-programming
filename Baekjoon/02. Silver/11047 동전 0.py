N, K = map(int, input().split())
coin_li = [int(input()) for i in range(N)]
count = 0

for i in reversed(range(N)):
    count += K // coin_li[i]
    K = K % coin_li[i]

print(count)
