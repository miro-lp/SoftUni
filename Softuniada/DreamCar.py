salary = float(input())
costs = float(input())
rise = float(input())
price_car = float(input())
months = int(input())

total_rise = 0
for i in range(months):
    total_rise += i * rise

save_money = (salary - costs) * months + total_rise

if save_money >= price_car:
    print("Have a nice ride!")
else:
    print(f"Work harder!")
