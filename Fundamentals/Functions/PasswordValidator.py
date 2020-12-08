def length_password(password):
    result = None
    if 6 <= len(password) <= 10:
        result = True
    else:
        result = False
    return result


def check_letters_digits(password):
    result = True
    for char in password:
        if not char.isalpha() and not char.isdigit():
            result = False
    return result


def are_two_digits(password):
    result = None
    digits = 0
    for i in password:
        if 48 <= ord(i) <= 57:
            digits += 1
    if digits >= 2:
        result = True
    else:
        result = False
    return result


password = input()

if length_password(password) and check_letters_digits(password) and are_two_digits(password):
    print("Password is valid")
else:
    if not length_password(password):
        print("Password must be between 6 and 10 characters")
    if not check_letters_digits(password):
        print("Password must consist only of letters and digits")
    if not are_two_digits(password):
        print("Password must have at least 2 digits")
