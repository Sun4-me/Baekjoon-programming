import sys, math

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [[[], []] for _ in range(7)]
for _ in range(n):
    s, y = map(int, input().split())
    arr[y][s].append(1)

ans = 0
for w, m in arr:
    ans += math.ceil(len(w) / k) + math.ceil(len(m) / k)
print(ans)
