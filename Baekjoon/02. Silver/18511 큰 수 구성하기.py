from itertools import product

n, m = map(int, input().split())
k = list(map(int, input().split()))
k.sort(reverse=True)
length = len(str(n))

while 1:
    num = list(product(k, repeat=length))
    for a in num:
        a_num = int("".join(map(str, a)))
        if a_num <= n:
            print(a_num)
            exit()
    length -= 1
