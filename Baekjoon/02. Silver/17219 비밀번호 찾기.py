import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pw_di = {}

for _ in range(n):
    st, pw = map(str, input().strip().split())
    pw_di[st] = pw

for _ in range(m):
    user_st = input().strip()
    print(pw_di[user_st])
