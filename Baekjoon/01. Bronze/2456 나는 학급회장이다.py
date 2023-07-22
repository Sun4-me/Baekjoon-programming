import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

score = [[0] * 3 for _ in range(3)]

for _ in range(N):
    a, b, c = map(int, input().split())
    score[0][a - 1] += a
    score[1][b - 1] += b
    score[2][c - 1] += c

total_score = [[idx, sum(sc)] for idx, sc in enumerate(score)]
max_score = max(map(lambda x: x[1], total_score))
candidate = list(filter(lambda x: x[1] == max_score, total_score))

if len(candidate) >= 2:
    max_three_count = max(map(lambda x: score[x[0]][2], candidate))
    candidate = list(filter(lambda x: score[x[0]][2] == max_three_count, candidate))
    max_two_count = max(map(lambda x: score[x[0]][1], candidate))
    candidate = list(filter(lambda x: score[x[0]][1] == max_two_count, candidate))

if len(candidate) >= 2:
    print(0, max_score)
else:
    print(candidate[0][0] + 1, candidate[0][1])
