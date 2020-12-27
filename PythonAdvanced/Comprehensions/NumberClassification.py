nums = list(map(int, input().split(", ")))

print(f"Positive: {', '.join([str(i) for i in nums if i >= 0])}")
print(f"Negative: {', '.join([str(i) for i in nums if i < 0])}")
print(f"Even: {', '.join([str(i) for i in nums if i % 2 == 0])}")
print(f"Odd: {', '.join([str(i) for i in nums if i % 2 == 1])}")
