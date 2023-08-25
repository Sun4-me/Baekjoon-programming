while True:
    data = list(map(int, input().split()))
    if len(data) == 1 and data[0] == -1:
        break

    result = 0
    for i in range(len(data) - 1):
        if data[i] % 2 == 0:
            if data[i] // 2 in data:
                result += 1

    print(result)
