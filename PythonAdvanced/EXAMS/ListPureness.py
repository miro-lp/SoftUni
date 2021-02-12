from collections import deque


def best_list_pureness(nums, k):
    pureness = sum([i * nums[i] for i in range(len(nums))])
    rotation = 0
    nums = deque(nums)
    result = [pureness, rotation]
    while k > 0:
        nums.rotate(1)
        p = sum([i * nums[i] for i in range(len(nums))])
        rotation += 1
        if p > result[0]:
            result = [p, rotation]
        k -= 1
    return f"Best pureness {result[0]} after {result[1]} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
