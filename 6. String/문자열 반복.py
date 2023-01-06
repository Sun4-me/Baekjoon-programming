T = int(input())

for _ in range(T):
    cnt, word = input().split()
    for i in word:
        print(i*int(cnt), end='')
    print()
