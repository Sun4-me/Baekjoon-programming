N, M = map(int,input().split())
card_list = list(map(int,input().split()))
max_sum = 0

for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            if card_list[a] + card_list[b] + card_list[c] > M:
                continue
            else:
                max_sum = max(max_sum, card_list[a] + card_list[b] + card_list[c])

print(max_sum)