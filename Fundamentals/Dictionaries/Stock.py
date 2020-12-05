text = input().split(" ")
search_products = input().split(" ")

menu = {}
for i in range(0, len(text) - 1, 2):
    menu[text[i]] = int(text[i + 1])

for product in search_products:
    if product in menu:
        print(f"We have {menu[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
