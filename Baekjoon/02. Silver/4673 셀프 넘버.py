num = set(range(1, 10001))
remove_num = set()


def self_num(n):
    for i in str(n):
        n += int(i)
    return n


for i in range(1, 10001):
    remove_num.add(self_num(i))

result = sorted(num - remove_num)

for i in result:
    print(i)
