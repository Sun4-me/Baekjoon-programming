n = int(input())
Q = [0] * 5
for i in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        Q[0] += 1
    elif x > 0:
        if y > 0:
            Q[1] += 1
        else:
            Q[4] += 1
    else:
        if y > 0:
            Q[2] += 1
        else:
            Q[3] += 1
for i in range(1,5):
    print(f'Q{i}: {Q[i]}')
print(f'AXIS: {Q[0]}')