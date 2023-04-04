word = input()
word_list = []

for a in range(1 , len(word) - 1):
    for b in range(1+a, len(word)):
        f_word = word[:a][::-1]
        s_word = word[a:b][::-1]
        t_word = word[b:][::-1]
        word_list.append(f_word+s_word+t_word)

word_list.sort()
print(word_list[0])
