n = int(input())

text_list = [input() for i in range(n)]

is_it_first = True
for index, symb in enumerate(text_list):
    if symb == "(":
        is_balanced = False
        is_it_first = False
        for i in range(index + 1, len(text_list)):
            if text_list[i] == ")":
                last_index = i
                is_balanced = True
                break
    elif symb == ")" and is_it_first:
        is_balanced = False
        break
    elif symb == ")" and index > last_index:
        is_balanced = False

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
