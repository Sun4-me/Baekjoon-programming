n, x = map(int,input().split())
a = list(map(int,input().split()))

for v in range(n):
    if a[v] < x :
        print(a[v], end=" ")