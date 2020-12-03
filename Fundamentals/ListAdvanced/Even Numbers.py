numbers = map(lambda x: int(x), input().split(", "))

even_index = []

for index, num in enumerate(numbers):
    if num % 2 == 0:
        even_index.append(index)

print(even_index)
