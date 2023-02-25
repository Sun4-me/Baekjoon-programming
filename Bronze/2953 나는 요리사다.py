max = 0
max_idx = 0

for i in range(1,6):
    s = sum(int(x) for x in input().split())
    if max < s :
        max = s
        max_idx = i
        
print(max_idx, max)