text = input()

cipher = ""

for i in text:
    cipher += chr(ord(i) + 3)

print(cipher)
