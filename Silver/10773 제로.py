import sys

num_li = []

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if num == 0:
        num_li.pop()
    else:
        num_li.append(num)

print(sum(num_li))
