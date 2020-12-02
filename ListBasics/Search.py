n = int(input())
word = input()

list_of_word = []

for i in range(n):
    current = input()
    list_of_word.append(current)

print(list_of_word)

for i in range(len(list_of_word) - 1, -1, -1):
    search_element = list_of_word[i]
    if word not in search_element:
        list_of_word.remove(search_element)

print(list_of_word)
