t = int(input())
for _ in range(t):
    j, n = map(int, input().split())

    data = []
    for _ in range(n):
        a, b = map(int, input().split())
        data.append(a * b)

    data.sort(reverse=True)
    result = 0
    for i in range(len(data)):
        j -= data[i]
        result += 1
        if j <= 0:
            break

    print(result)
