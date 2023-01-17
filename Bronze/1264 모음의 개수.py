while 1:
    a = input()
    if a == '#':
        break
    cnt = 0
    for b in a:
        if b in 'aeiouAEIOU':
            cnt += 1
    print(cnt)