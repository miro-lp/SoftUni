text = input().split(" ")

total_sum = []

if len(text[0]) >= len(text[1]):
    total_sum = [ord(i) for i in text[0]]

    for index, i in enumerate(text[1]):
        total_sum[index] *= int(ord(i))
else:
    for i in text[1]:
        total_sum.append(int(ord(i)))

    for index, i in enumerate(text[0]):
        total_sum[index] *= int(ord(i))

print(sum(total_sum))
