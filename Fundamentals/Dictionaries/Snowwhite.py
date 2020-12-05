from collections import defaultdict

dwarfs = {}
colors = {}
dwarfs_color = defaultdict(int)

while True:
    data = input()
    if data == "Once upon a time":
        break
    dwarf, color, body = data.split(" <:> ")
    if color not in colors:
        colors[color] = []
    if dwarf not in colors[color]:
        colors[color].append(dwarf)
    if (dwarf, color) not in dwarfs:
        dwarfs[(dwarf, color)] = int(body)
    else:
        if int(body) > dwarfs[(dwarf, color)]:
            dwarfs[(dwarf, color)] = int(body)

for clr in colors:
    for i in colors[clr]:
        dwarfs_color[(i, clr)] = len(colors[clr])
# dwarfs_color = dict(sorted(dwarfs_color.items(), key=lambda x: -x[1]))

dwarfs = dict(sorted(dwarfs.items(), key=lambda y: (-y[1], -dwarfs_color[y[0]])))

for i in dwarfs:
    dwarf, color = i
    print(f"({color}) {dwarf} <-> {dwarfs[i]}")