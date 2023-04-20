for _ in range(int(input())):
    num = list(map(int, input().split()))
    even = []
    for i in num:
        if i % 2 ==0:
            even.append(i)
    print(sum(even),min(even))
