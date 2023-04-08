candy = int(input())

cnt = 0 
while candy >= 0:
    if candy % 5 == 0:
        cnt += candy//5
        print(cnt)
        break
    candy -= 3
    cnt += 1
else:
    print(-1)