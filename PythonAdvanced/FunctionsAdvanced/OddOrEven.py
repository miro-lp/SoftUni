command = input()
nums = list(map(int, input().split()))

if command == "Odd":
    print(sum(filter(lambda x: x % 2 == 1, nums)) * len(nums))
else:
    print(sum(filter(lambda x: x % 2 == 0, nums)) * len(nums))
