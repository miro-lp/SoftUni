numbers = list(map(lambda n: int(n), input().split(", ")))

new_list = []
limit = 0

while limit < max(numbers):
    new_list = [i for i in numbers if limit < i <= (limit + 10)]
    limit += 10
    print(f"Group of {limit - 10}'s: {new_list}")
