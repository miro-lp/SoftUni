numbers = input().split(" ")

sorted_list = list(reversed(sorted(numbers)))

max_num = ""

for i in sorted_list:
    max_num += i

print(max_num)
