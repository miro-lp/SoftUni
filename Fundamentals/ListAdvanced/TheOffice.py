happiness = map(lambda x: int(x), input().split(" "))
factor = int(input())

happiness_factor = list(map(lambda x: x * factor, happiness))

avarage_happiness = sum(happiness_factor) / len(happiness_factor)
happy_people = 0

for i in happiness_factor:
    if i >= avarage_happiness:
        happy_people += 1
if happy_people >= len(happiness_factor) / 2:
    print(f"Score: {happy_people}/{len(happiness_factor)}. Employees are happy!")
else:
    print(f"Score: {happy_people}/{len(happiness_factor)}. Employees are not happy!")
