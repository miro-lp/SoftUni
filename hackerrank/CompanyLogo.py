from collections import defaultdict

s = input()

letters = defaultdict(int)

for l in s:
    letters[l] += 1

letters=dict(sorted(letters.items(), key= lambda x:(-x[1],x[0])))

print(*[f"{i} {letters[i]}" for i in letters][:3], sep="\n")