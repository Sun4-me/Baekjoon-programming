a = int(input())
b = int(input())
c = int(input())
tmp = list(str(a * b * c))

for i in range(10):
    print(tmp.count(str(i)))