import re

pattern = r"[456]\d{3}[-]?\d{4}[-]?\d{4}[-]?\d{4}$"
nums = ["0000","1111","2222","3333","4444","5555","6666","7777","8888","9999"]


n = int(input())
for _ in range(n):
    card = input()
    is_valid = True
    if re.match(pattern,card):
        if "-" in card:
            card = "".join(card.split("-"))
        for num in nums:
            if num in card:
                is_valid = False
                break
    else:
        is_valid = False

    if is_valid:
        print("Valid")
    else:
        print("Invalid")

