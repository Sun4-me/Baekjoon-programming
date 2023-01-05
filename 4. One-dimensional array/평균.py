n = int(input())
score = list(map(int,input().split()))

m = max(score)
newScore=[]

for i in score:
    newScore.append(i/m*100)

avg = sum(newScore)/n
print(avg)