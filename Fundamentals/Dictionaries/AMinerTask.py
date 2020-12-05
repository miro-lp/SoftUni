miner_quant = {}

while True:
    line = input()
    if line == "stop":
        break
    resource = line
    quantity = int(input())
    if resource not in miner_quant:
        miner_quant[resource] = 0
    miner_quant[resource] += quantity

for j in miner_quant:
    print(f"{j} -> {miner_quant[j]}")
