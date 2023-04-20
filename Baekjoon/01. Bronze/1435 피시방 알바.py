n = int(input())
com_li = list(map(int, input().split()))

refused_cnt  = 0
seated_li = []

for i in range(n):
    if com_li[i] in seated_li:
        refused_cnt += 1
    
    else :
        seated_li.append(com_li[i])

print(refused_cnt)
