def char_in_range(a, b):
    result = ""
    for i in range(ord(a) + 1, ord(b)):
        result += chr(i) + " "
    return result


first_char = input()
second_char = input()

print(char_in_range(first_char, second_char))
