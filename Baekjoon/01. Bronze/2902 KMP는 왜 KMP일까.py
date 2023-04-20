import sys

full_name = list(sys.stdin.readline().split("-"))
short_name = ""
for i in range(len(full_name)):
    short_name += full_name[i][0]

print(short_name)
