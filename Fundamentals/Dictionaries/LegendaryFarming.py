is_acomplished = False

farming_stuff = {"shards": 0, "motes": 0, "fragments": 0}
win_key = ""
while True:
    text = input().split(" ")

    for i in range(len(text)):
        if i % 2 != 0:
            text[i] = text[i].lower()
            if text[i] not in farming_stuff:
                farming_stuff[text[i]] = 0
            farming_stuff[text[i]] += int(text[i - 1])
            if farming_stuff[text[i]] >= 250 and (text[i] == "shards" or text[i] == "motes" or text[i] == "fragments"):
                is_acomplished = True
                win_key = text[i]
                break
    if is_acomplished:
        break

farming_stuff[win_key] -= 250

if win_key == "shards":
    print("Shadowmourne obtained!")
elif win_key == "fragments":
    print("Valanyr obtained!")
elif win_key == "motes":
    print("Dragonwrath obtained!")

key_materials = {}
junk_materials = {}
for i in farming_stuff:
    if i == "shards" or i == "motes" or i == "fragments":
        key_materials[i] = farming_stuff[i]
    else:
        junk_materials[i] = farming_stuff[i]

key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
for i in key_materials:
    print(f"{i}: {key_materials[i]}")

junk_materials = dict(sorted(junk_materials.items(), key=lambda x: x[0]))

for i in junk_materials:
    print(f"{i}: {junk_materials[i]}")
