i = 1

while True:
    result = 0
    L, P, V = map(int, input().split())

    if L + P + V == 0:
        break

    result = ((V // P) * L) + min((V % P), L)
    print("Case {}: {}".format(i, result))
    i += 1
