fires_cells = input().split("#")
water = int(input())

fires_cells_list = []

for i in fires_cells:
    fires_cells_list += i.split(" = ")

total_effort = 0
total_fire = 0

print("Cells:")
for i in range(0, len(fires_cells_list), 2):
    if fires_cells_list[i] == "High" and 81 <= int(fires_cells_list[i + 1]) <= 125 \
            and water >= int(fires_cells_list[i + 1]):
        water -= int(fires_cells_list[i + 1])
        total_fire += int(fires_cells_list[i + 1])
        total_effort += int(fires_cells_list[i + 1]) * .25
        print(f" - {fires_cells_list[i + 1]}")
    elif fires_cells_list[i] == "Medium" and 51 <= int(fires_cells_list[i + 1]) <= 80 \
            and water >= int(fires_cells_list[i + 1]):
        water -= int(fires_cells_list[i + 1])
        total_fire += int(fires_cells_list[i + 1])
        total_effort += int(fires_cells_list[i + 1]) * .25
        print(f" - {fires_cells_list[i + 1]}")
    elif fires_cells_list[i] == "Low" and 1 <= int(fires_cells_list[i + 1]) <= 50 \
            and water >= int(fires_cells_list[i + 1]):
        water -= int(fires_cells_list[i + 1])
        total_fire += int(fires_cells_list[i + 1])
        total_effort += int(fires_cells_list[i + 1]) * .25
        print(f" - {fires_cells_list[i + 1]}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
