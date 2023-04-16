def Rev(x):
    x = str(x)  
    x = x[::-1]
    return int(x)
X, Y = map(int, input().split())
print(Rev(Rev(X) + Rev(Y)))