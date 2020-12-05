product_stock = {}

while True:
    text = input()
    if text == "statistics":
        break
    key_value = text.split(": ")
    if key_value[0] not in product_stock:
        product_stock[key_value[0]] = int(key_value[1])
    else:
        product_stock[key_value[0]] += int(key_value[1])

print("Products in stock:")
for i in product_stock:
    print(f"- {i}: {product_stock[i]}")
print(f"Total Products: {len(product_stock)}")
print(f"Total Quantity: {sum(product_stock.values())}")
