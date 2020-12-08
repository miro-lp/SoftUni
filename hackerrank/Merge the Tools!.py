import textwrap


def merge_the_tools(string, k):
    list_wrap = textwrap.wrap(string, k)
    list_new = []
    for i in list_wrap:
        new_i = ""
        for j in i:
            if j not in new_i:
                new_i += j
        list_new.append(new_i)
    for w in list_new:
        print(w)


string, k = input(), int(input())
merge_the_tools(string, k)
