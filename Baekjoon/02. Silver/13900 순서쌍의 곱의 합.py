N = int(input())
nums = list(map(int, input().split()))

sum_nums = sum(nums)
res = 0

for n in nums:
    sum_nums -= n
    res += sum_nums * n

print(res)
