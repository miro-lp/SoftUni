nums = list(map(int, input().split()))

negative = list(filter(lambda x: x < 0, nums))
positive = list(filter(lambda x: x > 0, nums))

print(sum(negative))
print(sum(positive))

if abs(sum(negative)) > sum(positive):
    print("The negatives are stronger than the positives")
elif abs(sum(negative)) < sum(positive):
    print("The positives are stronger than the negatives")
