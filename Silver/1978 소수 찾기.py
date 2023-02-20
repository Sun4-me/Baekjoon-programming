N = int(input())
nums = list(map(int, input().split()))
cnt = 0

for x in nums:
    for y in range(2, x+1):
        if x % y == 0:
            if x == y :
                cnt += 1

            break

print(cnt)