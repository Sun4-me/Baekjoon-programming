import sys, heapq

input = sys.stdin.readline

n = int(input())
win = int(input())
nums = []

for _ in range(n - 1):
    num = int(input())
    heapq.heappush(nums, (-num, num))

cnt = 0
while nums:
    num = heapq.heappop(nums)[1]
    if num >= win:
        num -= 1
        win += 1
        cnt += 1
        heapq.heappush(nums, (-num, num))

print(cnt)
