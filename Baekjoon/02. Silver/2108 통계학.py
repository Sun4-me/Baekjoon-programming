import sys

input = sys.stdin.readline

n = int(input())
num_li = []

for i in range(n):
    num_li.append(int(input()))

num_li.sort()

print(round(sum(num_li) / len(num_li)))
print(num_li[len(num_li) // 2])


di = dict()
for i in num_li:
    if i in di:
        di[i] += 1
    else:
        di[i] = 1

mx = max(di.values())
mx_di = []

for i in di:
    if mx == di[i]:
        mx_di.append(i)

if len(mx_di) > 1:
    print(mx_di[1])
else:
    print(mx_di[0])

print(max(num_li) - min(num_li))
