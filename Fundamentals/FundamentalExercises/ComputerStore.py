total_price = 0

while True:
    command = input()
    if command == "regular" or command == "special":
        break
    order = float(command)
    if order < 0:
        print("Invalid price!")
    else:
        total_price += order

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {total_price*.2:.2f}$")
    print("-----------")
    if command == "regular":
        print(f"Total price: {total_price*1.2:.2f}$")
    else:
        print(f"Total price: {total_price*1.2*.9:.2f}$")