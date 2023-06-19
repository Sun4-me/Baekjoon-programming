unsorted_li = list(map(int, input().split()))
result = [1, 2, 3, 4, 5]

while True:
    for i in range(len(unsorted_li) - 1):
        if unsorted_li[i] > unsorted_li[i + 1]:
            unsorted_li[i], unsorted_li[i + 1] = unsorted_li[i + 1], unsorted_li[i]
            print(" ".join(map(str, unsorted_li)))

    if unsorted_li == result:
        break
