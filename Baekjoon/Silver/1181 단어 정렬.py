import sys

N = int(sys.stdin.readline())
words = list(set(str(sys.stdin.readline().strip()) for _ in range(N)))
words.sort()
words.sort(key=lambda x: len(x))

for i in words:
    print(i)