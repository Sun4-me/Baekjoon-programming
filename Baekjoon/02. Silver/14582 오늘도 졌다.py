geminis = list(map(int, input().strip().split()))
startlink = list(map(int, input().strip().split()))
g_sum, s_sum, flag = 0, 0, False
for i in range(9):
    g_sum += geminis[i]
    if g_sum > s_sum:
        flag = True
    s_sum += startlink[i]
print("Yes" if g_sum < s_sum and flag else "No")
