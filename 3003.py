chess = [1,1,2,2,2,8]
y_list = list(map(int,input().split()))
for v in range(6):
    print(chess[v]-y_list[v],end=" ")