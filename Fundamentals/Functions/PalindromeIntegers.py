def get_palindrome_int(number):
    backword_number = ""
    for i in range(-1, -len(number) - 1, -1):
        backword_number += number[i]
    if backword_number == number:
        return True
    else:
        return False


list_numbers = input().split(", ")

for i in list_numbers:
    print(get_palindrome_int(i))
