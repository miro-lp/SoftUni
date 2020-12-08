first = int(input())
second = int(input())
third = int(input())
count_students = int(input())

helped_count = 0
hours = 0
total_efficiency = first + second + third

while helped_count < count_students:
    hours += 1
    if hours % 4 == 0:
        continue
    helped_count += total_efficiency

print(f"Time needed: {hours}h.")
