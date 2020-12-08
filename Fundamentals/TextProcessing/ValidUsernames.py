passwords = input().split(", ")

valid_passwords = []

for password in passwords:
    is_length = False
    is_letter = False
    is_other_symbols = False

    if 3 <= len(password) <= 16:
        is_length = True
    for i in password:
        if not (i.isalnum() or i == "-" or i == "_"):
            is_other_symbols = True
    if not is_other_symbols:
        is_letter = True
    if is_length and is_letter:
        valid_passwords.append(password)

for i in valid_passwords:
    print(i)
