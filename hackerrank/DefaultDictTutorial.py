from collections import defaultdict

n, m = map(int, input().split())
words = defaultdict(list)
searched_word = []
for i in range(1, n + 1):
    words[input()].append(i)
for _ in range(m):
    searched_word.append(input())

for w in searched_word:
    if w in words:
        print(" ".join(map(str, words[w])))
    else:
        print("-1")
