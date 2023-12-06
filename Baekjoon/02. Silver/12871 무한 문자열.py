s = input()
t = input()

slen, tlen = len(s), len(t)

if slen * t == tlen * s:
    print(1)
else:
    print(0)
