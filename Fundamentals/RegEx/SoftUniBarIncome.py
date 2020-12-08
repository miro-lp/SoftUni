import re

pattern = r"%([A-Z][a-z]+)%[^|$%.]*<(\w+)>[^|$%.]*\|(\d+)\|[^|$%.0-9]*(\d+[\.\d+]*)\$"
# %([A-Z][a-z]+)%\w*<(\w+)>\w*\|(\d+)\|[A-z]*(\d+[\.\d+]*)\$
total_income = 0
while True:
    data = input()
    if data == "end of shift":
        break
    matches = re.findall(pattern, data)
    if len(matches) > 0:
        name, product, count, price = matches[0]
        income = int(count) * float(price)
        print(f"{name}: {product} - {income:.2f}")
        total_income += income

print(f"Total income: {total_income:.2f}")
