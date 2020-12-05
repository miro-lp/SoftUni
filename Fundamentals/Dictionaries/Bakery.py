text = input().split(" ")

bakery_menu = {}
for i in range(0, len(text) - 1, 2):
    bakery_menu[text[i]] = int(text[i + 1])

print(bakery_menu)
