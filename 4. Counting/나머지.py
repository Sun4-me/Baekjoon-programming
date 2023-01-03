numbers = []

for _ in range(10):
    i = int(input())
    numbers.append(i%42)

newNumbers = set(numbers)

print(len(newNumbers))