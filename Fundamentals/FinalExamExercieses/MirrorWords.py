import re

txt = input()

ptrn = r"([#|@])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
matches = re.findall(ptrn, txt)

mirror_words = []

for i in matches:
    _, word_1, word_2 = i
    if word_1 == word_2[::-1]:
        mirror_words.append(word_1 + " <=> " + word_2)

if len(matches) == 0:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{len(matches)} word pairs found!")
    if len(mirror_words) == 0:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        print(", ".join(mirror_words))
