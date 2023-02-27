nums = []

for _ in range(7):
    num = int(input())
    nums.append(num)

odd_li = []
odd_exsist = False

for i in nums:
    if i % 2 !=0 :
        odd_li.append(i)
        odd_exsist = True

if odd_exsist == False :
    print(-1)

else : 
    print(sum(odd_li))
    print(min(odd_li))