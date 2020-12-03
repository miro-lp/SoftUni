def sum_of_integers(num):
    sums = 0
    for i in range(len(num)):
        sums += int(num[i])
    return sums


numbers = input().split(" ")
text = list(input())

new_word = ""
for num in numbers:
    index = sum_of_integers(num)
    if index <= len(text) - 1:
        new_word += text[index]
        text.pop(index)
    else:
        while len(text) - 1 < index:
            index -= len(text)
        new_word += text[index]
        text.pop(index)

print(new_word)
