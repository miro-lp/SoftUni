deck_of_cards = input().split(" ")
shuffle_count = int(input())

for i in range(shuffle_count):
    shuffled_cards = []

    for i in range(int(len(deck_of_cards) / 2)):
        first_card = deck_of_cards[i]
        second_card = deck_of_cards[i + (len(deck_of_cards) // 2)]
        shuffled_cards.append(first_card)
        shuffled_cards.append(second_card)
    deck_of_cards = shuffled_cards

print(shuffled_cards)
