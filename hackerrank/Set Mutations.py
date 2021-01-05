n = int(input())
set_1 = set(map(int,input().split()))
m = int(input())

for _ in range(m):
    command, len_set_2 = input().split()
    set_2 = set(map(int,input().split()))
    if command == "intersection_update":
        set_1.intersection_update(set_2)
    elif command == "update":
        set_1.update(set_2)
    elif command == "symmetric_difference_update":
        set_1.symmetric_difference_update(set_2)
    elif command == "difference_update":
        set_1.difference_update(set_2)

print(sum(set_1))