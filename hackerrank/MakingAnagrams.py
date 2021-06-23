def make_anagram(a, b):
    a_1 = list(a)
    b_1 = list(b)
    for ch in a:
        if ch in b_1:
            b_1.remove(ch)
            a_1.remove(ch)
    return len(a_1) + len(b_1)


a = input()

b = input()

res = make_anagram(a, b)

print(res)


