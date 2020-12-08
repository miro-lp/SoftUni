from itertools import permutations
text, num = input().split()

print(*[("".join(i)) for i in list(sorted(permutations(text,int(num),)))],sep="\n")