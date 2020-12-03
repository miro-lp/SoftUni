# health_popul = list(map(int, input().split(", ")))
# min_health = int(input())
#
# max_health = max(health_popul)
# is_it_possible_distr = False
# counter = 0
# for index, i in enumerate(health_popul):
#     if i < min_health:
#         health_popul[index] = min_health
#         counter += min_health - i
#     elif i == max_health:
#         health_popul[index] -= counter
#         if health_popul[index] < min_health:
#             print("No equal distribution possible")
#             is_it_possible_distr = True
#             break
# if not is_it_possible_distr:
#     print(health_popul)
numbers = [int(num) for num in input().split(", ")]
minimum_wealth = int(input())

for i in range(len(numbers)):
    if numbers[i] < minimum_wealth:
        c = minimum_wealth - numbers[i]
        max_number = max(numbers)
        if max_number - c >= minimum_wealth:
            numbers[numbers.index(max_number)] -= c
            numbers[i] += c
if sum(numbers) >= len(numbers) * minimum_wealth:
    print(numbers)
else:
    print("No equal distribution possible")