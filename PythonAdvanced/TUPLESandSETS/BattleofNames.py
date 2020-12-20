n = int(input())

value_line = 0
set_odd = set()
set_even = set()

for i in range(n):
    name = input()
    value = 0
    value_line += 1
    for i in name:
        value += ord(i)
    value = value // value_line
    if value % 2 == 0:
        set_even.add(value)
    else:
        set_odd.add(value)
if sum(set_odd) == sum(set_even):
    print(", ".join([str(i) for i in (set_even | set_odd)]))
elif sum(set_odd) > sum(set_even):
    print(", ".join([str(i) for i in (set_odd - set_even)]))
else:
    print(", ".join([str(i) for i in (set_odd ^ set_even)]))
