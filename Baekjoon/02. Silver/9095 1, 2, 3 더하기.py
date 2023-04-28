t = int(input())


def fibo(n):
    if n == 1:
        return 1

    elif n == 2:
        return 2

    elif n == 3:
        return 4

    else:
        return fibo(n - 1) + fibo(n - 2) + fibo(n - 3)


for i in range(t):
    n = int(input())
    print(fibo(n))
