from itertools import groupby

s = input()

for key, group in groupby(list(s),lambda x:x[0]):
    print((len(list(group)),int(key)), end=" ")
