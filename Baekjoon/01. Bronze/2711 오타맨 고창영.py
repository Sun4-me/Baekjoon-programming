for _ in range(int(input())):
    n, string = input().split()
    n = int(n)
    print(string[: n - 1], string[n:], sep="")
