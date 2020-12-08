import re

total_money = 0
furniture = []
pattern = r">>([A-z]+)<<(\d+\.?\d*)!(\d+)"

line = input()

while not line == "Purchase":
    matches = re.findall(pattern, line)
    if len(matches) > 0:
        item, price, count = matches[0]
        furniture.append(item)
        total_money += float(price) * int(count)
    line = input()

print("Bought furniture:")
for key in furniture:
    print(key)
print(f"Total money spend: {total_money:.2f}")
