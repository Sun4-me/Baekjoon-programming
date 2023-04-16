def FA(x):
    k = str(x)
    if x == int(k[0])*len(k):
        return "FA"
    return FA(int(k[0])*len(k))

x = int(input())
print(FA(x))