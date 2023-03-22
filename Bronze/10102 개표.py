v = int(input())
li = list(input())
A=B=0

for v in li:
    if v =='A':
        A+=1
    else:
        B+=1

if A>B:
    print('A')
elif A==B:
    print('Tie')
else:
    print('B')