import sys

dic = {}
N = int(sys.stdin.readline())
for n in range(N):
    a = int(sys.stdin.readline())
    if a in dic.keys():
        dic[a] += 1
    else:
        dic[a] = 1

    if n == 0:
        temp = a
    if dic[temp] == dic[a]:
        temp = min(temp, a)
    elif dic[temp] < dic[a]:
        temp = a
print(temp)
