t = int(input())

for _ in range(t):
    l = [i for i in range(65, 91)]
    for i in input():
        l[ord(i) - 65] = 0
    print(sum(l))
