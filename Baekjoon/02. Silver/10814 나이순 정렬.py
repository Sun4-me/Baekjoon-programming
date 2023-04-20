n = int(input())
member = []

for i in range(n):
    age, name = map(str,input().split())
    age = int(age)
    member.append([age, name])

member.sort(key = lambda x : x[0])

for j in range(n) :
    print(member[j][0],member[j][1])