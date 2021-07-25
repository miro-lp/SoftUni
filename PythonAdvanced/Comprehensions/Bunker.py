ctgrs = input().split(", ")
bunker = {i: [] for i in ctgrs}
n = int(input())

total_qtity = 0
tota_qlity = 0
for _ in range(n):
    categ, item, info = input().split(" - ")
    qtity, qlity = [int(j) for i in info.split(";") for j in i.split(":") if str(j).isdigit()]
    total_qtity += qtity
    tota_qlity += qlity
    bunker[categ].append(item)

print(f"Count of items: {total_qtity}")
print(f"Average quality: {tota_qlity / len(bunker):.2f}")
print("\n".join([f"{i} -> {', '.join([j for j in bunker[i]])}" for i in bunker]))

