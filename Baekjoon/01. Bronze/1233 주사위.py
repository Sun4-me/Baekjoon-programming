s1, s2, s3 = map(int, input().strip().split())
s1_arr = [element for element in range(1, 1 + s1)]
s2_arr = [element for element in range(1, 1 + s2)]
s3_arr = [element for element in range(1, 1 + s3)]
s4_arr = [a + b + c for a in s1_arr for b in s2_arr for c in s3_arr]
arr = [0] * 81
for element in s4_arr:
    arr[element] += 1
print(arr.index(max(arr)))
