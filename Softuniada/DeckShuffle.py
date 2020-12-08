n = int(input())
indexes = [int(i) for i in input().split()]

deck = []

for i in range(1, n + 1):
    deck.append(i)

for j in indexes:
    l_1 = deck[:j]
    l_2 = deck[j:]
    deck.clear()
    if len(l_1) >= len(l_2):
        for k in range(len(l_1)):
            deck.append(l_1[k])
            if k < len(l_2):
                deck.append(l_2[k])
    else:
        for k in range(len(l_2)):
            if k < len(l_1):
                deck.append(l_1[k])
            deck.append(l_2[k])

deck = [str(i) for i in deck]
print(" ".join(deck))
