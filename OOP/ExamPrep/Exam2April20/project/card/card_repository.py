class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card):
        if card.name in [c.name for c in self.cards]:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        for c in self.cards:
            if c.name == card:
                self.cards.remove(c)
                self.count -= 1
                break

    def find(self, name):
        for c in self.cards:
            if name == c.name:
                return c

    def __iter__(self):
        return self.cards
