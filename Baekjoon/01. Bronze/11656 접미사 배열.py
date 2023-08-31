tmp = input()
answer = []

for i in range(len(tmp)):
    answer.append(tmp[i:])

answer.sort()

for i in answer:
    print(i)
