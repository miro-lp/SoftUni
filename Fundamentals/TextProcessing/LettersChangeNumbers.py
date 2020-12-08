line = input().split()

sum = 0

for text in line:
    num = int(text[1:len(text) - 1])

    if text[0].isupper():
        divider = ord(text[0]) - 64
        num /= divider
    else:
        myltipl = ord(text[0]) - 96
        num *= myltipl

    if text[len(text) - 1].isupper():
        subt = ord(text[len(text) - 1]) - 64
        num -= subt
    else:
        add = ord(text[len(text) - 1]) - 96
        num += add
    sum += num

print(f"{sum:.2f}")
