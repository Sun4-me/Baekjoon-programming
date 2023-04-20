import sys

num_list = []

for _ in range(int(input())):
    num_list.append(int(sys.stdin.readline()))   

num_list.sort()

for i in num_list:
    print(i)