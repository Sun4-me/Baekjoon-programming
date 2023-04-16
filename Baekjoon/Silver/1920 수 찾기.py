n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

A.sort()			

for i in B:
    lt, rt = 0, n - 1
    flag = False
    
    while lt <= rt:
        mid = (lt + rt) // 2
        if i == A[mid]:
            flag = True
            print(1)
            break
        elif i > A[mid]:
            lt = mid + 1
        else:
            rt = mid - 1

    if flag is False:
        print(0)