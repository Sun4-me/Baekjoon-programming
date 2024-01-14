n = int(input())
tmp = [float(input()) for i in range(7)]
tmp.sort()
for i in range(n - 7):
    cnt = float(input())
    if tmp[6] > cnt:
        tmp.pop()
        tmp.append(cnt)
    tmp.sort()
for i in tmp:
    print("%.3f" % (i))
