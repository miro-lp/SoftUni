n = int(input())

set_max_size = set()

for i in range(n):
    data = input().split("-")
    set_1 = set()
    set_2 = set()
    sets = [set_1, set_2]
    for i in range(len(data)):
        a, b = data[i].split(",")
        for j in range(int(a), int(b) + 1):
            sets[i].add(j)
    if len(set_1.intersection(set_2)) > len(set_max_size):
        set_max_size.clear()
        set_max_size = set_1.intersection(set_2)

print(f"Longest intersection is [{', '.join([str(i) for i in sorted(set_max_size)])}] with length {len(set_max_size)}")
