numbers = [i for i in range(1,31)]

for _ in range(28):
    i = int(input())
    numbers.remove(i)

print(min(numbers))
print(max(numbers))