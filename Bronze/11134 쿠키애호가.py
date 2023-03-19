for _ in range(int(input())):
    n, c = map(int,input().split())
    res = n // c
    if n%c != 0:
        res+=1
    print(res)