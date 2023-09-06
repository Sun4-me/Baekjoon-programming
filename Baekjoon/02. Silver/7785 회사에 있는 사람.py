import sys

input = sys.stdin.readline

N = int(input())
company = {}
for _ in range(N):
    man, state = input().rstrip().split()
    if state == "enter":
        company[man] = True
    else:
        del company[man]

print("\n".join(sorted(company.keys(), reverse=True)))
