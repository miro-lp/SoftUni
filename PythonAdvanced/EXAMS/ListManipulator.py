def list_manipulator(nums, command, position, *args):
    if command == "add":
        if position == "beginning":
            nums = list(args) + nums
        elif position == "end":
            nums = nums + list(args)
    elif command == "remove":
        if position == "beginning":
            if len(args) == 0:
                nums = nums[1:]
            elif len(args) == 1:
                nums = nums[args[0]:]
        elif position == "end":
            if len(args) == 0:
                nums = nums[:-1]
            elif len(args) == 1:
                nums = nums[:-args[0]]
    return nums

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))


