phone_book = {}

while True:
    data = input().split("-")
    if len(data) < 2:
        n = int(data[0])
        break
    phone_book[data[0]] = data[1]

for i in range(n):
    name = input()
    if name in phone_book:
        print(f"{name} -> {phone_book[name]}")
    else:
        print(f"Contact {name} does not exist.")
