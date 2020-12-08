n = int(input())
sum_of_char = 0
for i in range(n):
    letter = input()
    sum_of_char += int(ord(letter))

print(f"The sum equals: {sum_of_char}")
