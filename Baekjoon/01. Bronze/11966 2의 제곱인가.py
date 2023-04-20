N = int(input())
tmp = [2**i for i in range(31)]

if N in tmp:
    print(1)
else:
    print(0)