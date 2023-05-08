import sys

input = sys.stdin.readline

noFBI = True
for i in range(1, 6):
    name = input().rstrip()
    if "FBI" in name:
        print(i, end=" ")
        noFBI = False
if noFBI:
    print("HE GOT AWAY!")
