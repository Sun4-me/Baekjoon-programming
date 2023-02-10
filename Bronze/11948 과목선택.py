A_li=[]
E_li=[]

for _ in range(4):
    A_li.append(int(input()))

for _ in range(2):
    E_li.append(int(input()))

A_li.sort()
E_li.sort()

score = sum(A_li[1:4]) + E_li[1]
print(score)