text = input()

dictionary = {}

for i in text:
    if i != " ":
        if i not in dictionary:
            dictionary[i] = 0
        dictionary[i] += 1

for j in dictionary:
    print(f"{j} -> {dictionary[j]}")
