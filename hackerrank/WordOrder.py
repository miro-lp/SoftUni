n = int(input())

count_words_rep = {}

for i in range(n):
    word = input()
    if word not in count_words_rep:
        count_words_rep[word] = 1
    else:
        count_words_rep[word] += 1

print(len(count_words_rep))
print(*list(count_words_rep.values()))
