import sys

while True:
    words = sys.stdin.readline().rstrip("\n")

    if not words:
        break

    l, u, d, s = 0, 0, 0, 0
    for each in words:
        if each.islower():
            l += 1
        elif each.isupper():
            u += 1
        elif each.isdigit():
            d += 1
        elif each.isspace():
            s += 1

    print(l, u, d, s)
