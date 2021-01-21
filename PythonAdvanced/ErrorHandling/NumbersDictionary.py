from collections import defaultdict

nums_dict = defaultdict(int)
line = input()

nums = []
while line != "Search":
    nums.append(line)
    line = input()

for i in range(0, len(nums) - 1, 2):
    try:
        nums_dict[nums[i]] = int(nums[i + 1])
    except ValueError:
        print("The variable number must be an integer")

nums_dict = dict(nums_dict)
if line == "Search":
    line = input()
    while line != "Remove":
        try:
            print(nums_dict[line])
        except KeyError:
            print("Number does not exist in dictionary")
        line = input()
if line == "Remove":
    line = input()
    while line != "End":
        try:
            nums_dict.pop(line)
        except KeyError:
            print("Number does not exist in dictionary")
        line = input()

print(nums_dict)
