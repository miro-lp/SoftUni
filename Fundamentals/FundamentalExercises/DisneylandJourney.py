budget = float(input())
months = int(input())

money = 0
for i in range(1, months+1):
    if i % 2 !=0 and i !=1:
        money *= .84
    if i %4 ==0:
        money*=1.25
    money +=.25*budget

if money>=budget:
    print(f"Bravo! You can go to Disneyland and you will have {money-budget:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {budget-money:.2f}lv. more.")
