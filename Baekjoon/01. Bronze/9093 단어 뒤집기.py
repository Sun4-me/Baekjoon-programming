import sys

T = int(sys.stdin.readline())
 
for _ in range(T):
    words = sys.stdin.readline().rstrip().split()
 
    for word in words:
        print(word[::-1], end=' ')
    print()