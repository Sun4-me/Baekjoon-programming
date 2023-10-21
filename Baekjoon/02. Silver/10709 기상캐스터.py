h, w = map(int, input().split())
city = []
answer = [[0] * w for i in range(h)]
cloud = False
for _ in range(h):
    city.append(list(map(str, input())))
for i in range(h):
    for j in range(w):
        if cloud == False and city[i][j] == ".":
            answer[i][j] = -1
        elif city[i][j] == "c":
            cloud = True
            answer[i][j] = 0
            num = 1
        elif cloud == True and city[i][j] == ".":
            answer[i][j] = num
            num += 1
    cloud = False
    num = 1
for i in range(h):
    for j in range(w):
        print(answer[i][j], end=" ")
    print()
