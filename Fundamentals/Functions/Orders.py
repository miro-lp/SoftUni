def total_price(product, quantity):
    price = 0
    if product == "coffee":
        price = 1.5
    elif product == "water":
        price = 1.0
    elif product == "coke":
        price = 1.4
    elif product == "snacks":
        price = 2.0
    result = price * quantity
    return result


product = input()
quantity = int(input())

finall_price = total_price(product, quantity)
print(f"{finall_price:.2f}")
