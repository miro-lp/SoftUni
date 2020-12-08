days = int(input())
budget = float(input())
people = int(input())
fuel_per_km = float(input())
food_per_day = float(input())
price_room = float(input())

if people > 10:
    hotel_expenses = people * price_room * .75
else:
    hotel_expenses = people * price_room

total_expenses_day = hotel_expenses + food_per_day * people
current_expenses = total_expenses_day * days

for i in range(1, days + 1):
    km_day = float(input())
    current_expenses += km_day * fuel_per_km
    if (i % 3 == 0 or i % 5 == 0) and not i % 7 == 0:
        current_expenses *= 1.4
    if i % 7 == 0:
        current_expenses -= current_expenses / people
    if current_expenses > budget:
        break

if current_expenses > budget:
    print(f"Not enough money to continue the trip. You need {current_expenses - budget:.2f}$ more.")
else:
    print(f"You have reached the destination. You have {budget - current_expenses:.2f}$ budget left.")
