import re

pattern = r"@#+([A-Z][A-Z|a-z|0-9]{4,}[A-Z])@#+"
pattern_digits = r"(\d)"

n = int(input())

for i in range(n):
    text = input()
    if re.search(pattern, text):
        digits = re.findall(pattern_digits, text)
        product = ""
        if len(digits)>0:
            for i in digits:
                product += i
            print(f"Product group: {product}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")