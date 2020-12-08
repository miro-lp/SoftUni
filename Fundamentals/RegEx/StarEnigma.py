import re

n = int(input())

pattern_count = r"([starSTAR])"
pattern_info = r"@([A-Z a-z]+)[^@!:\>\-]*[:]\d+[^@!:\>\-]*!([A D])![^@!:\>\-]*\->\d+"
all_info = {"A": [], "D": []}
for i in range(n):
    text = input()
    count = re.findall(pattern_count, text)
    dec_text = ""
    for l in text:
        dec_text += chr(ord(l) - len(count))
    info = re.findall(pattern_info, dec_text)
    for city, attack_type in info:
        all_info[attack_type].append(city)
        all_info[attack_type].sort()


print(f"Attacked planets: {len(all_info['A'])}")
for j in all_info['A']:
    print(f"-> {j}")
print(f"Destroyed planets: {len(all_info['D'])}")
for j in all_info['D']:
    print(f"-> {j}")
