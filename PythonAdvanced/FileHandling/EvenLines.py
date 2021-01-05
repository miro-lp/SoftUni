with open("text.txt", "r") as f:
    lines = f.readlines()

hints = [".", ",", "-", "!", "?"]

for i in range(len(lines)):
    if i % 2 == 0:
        print(" ".join(["".join(["@" if c in hints else c for c in w]) for w in lines[i].split()[::-1]]))
