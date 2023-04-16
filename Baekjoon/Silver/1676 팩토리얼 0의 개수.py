n = int(input())

def factorial(x):
    res = 1
    for i in range(x):
        res = res * (x-i)
    return res

cnt = 0
k = str(factorial(n))

for i in range(len(k)-1,1,-1):
    if k[i] == "0":
        cnt += 1
    else:
        break
    
print(cnt)