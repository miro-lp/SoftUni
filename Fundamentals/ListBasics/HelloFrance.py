items_prices = list(map(lambda x: x.split("->"), input().split("|")))
budget = float(input())

prices = []

for i in items_prices:
    if (i[0] == "Clothes" and float(i[1]) <= 50) or (i[0] == "Shoes" and float(i[1]) <= 35) or (
            i[0] == "Accessories" and float(i[1]) <= 20.5):
        prices.append(float(i[1]))

prices_profit = []
profit = 0

for price in prices:
    if price <= budget:
        budget -= price
        prices_profit.append(price * 1.4)
        profit += price * .4

for i in prices_profit:
    print(f"{i:.2f}",end=" ")
print()

print(f"Profit: {profit:.2f}")

if sum(prices_profit) + budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
