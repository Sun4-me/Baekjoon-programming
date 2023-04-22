n = int(input())

F = [0, 1]

for i in range(0, 90):
    F.append(F[i] + F[i + 1])

print(F[n])
