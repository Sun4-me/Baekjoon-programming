X_list = []
Y_list = []
for _ in range(3):
    x, y = map(int, input().split())
    X_list.append(x)
    Y_list.append(y)

for i in range(3):
    if X_list.count(X_list[i]) == 1:
        x4 = X_list[i]
    if Y_list.count(Y_list[i]) == 1:
        y4 = Y_list[i]
print(x4, y4)