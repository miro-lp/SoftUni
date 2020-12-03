electrons = int(input())

layers = []
counter = 1
while electrons > 0:
    shell = 2 * counter ** 2
    electrons -= shell
    counter += 1
    if electrons < 0:
        shell -= abs(electrons)
        layers.append(shell)
    else:
        layers.append(shell)

print(layers)
