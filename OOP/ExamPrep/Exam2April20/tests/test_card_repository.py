import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard



class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        self.cards = CardRepository()


    def test_init__count__list(self):
        self.assertEqual(0, len(self.cards.cards))
        self.assertEqual(0, self.cards.v_count)

    def test_add_player_when_doesnt_exist(self):
        card_1 = MagicCard("Dama")
        self.cards.add(card_1)
        self.assertEqual(1, len(self.cards.cards))
        self.assertEqual(1, self.cards.v_count)

    def test_add_player_when_exist(self):
        card_1 = MagicCard("Dama")
        self.cards.add(card_1)
        with self.assertRaises(ValueError) as ex:
            self.cards.add(card_1)
        self.assertEqual("Card Dama already exists!", str(ex.exception))
        self.assertEqual(1, len(self.cards.cards))
        self.assertEqual(1, self.cards.v_count)

    def test_remove_when_empty_str(self):
        with self.assertRaises(ValueError) as ex:
            self.cards.remove("")
        self.assertEqual("Card cannot be an empty string!", str(ex.exception))

    def test_remove_when_has_str(self):
        card_1 = MagicCard("Dama")
        self.cards.add(card_1)
        self.cards.remove("Dama")
        self.assertEqual(0, len(self.cards.cards))
        self.assertEqual(0, self.cards.v_count)

    def test_find(self):
        card_1 = MagicCard("Dama")
        self.cards.add(card_1)
        result = self.cards.find("Dama")
        self.assertEqual("Dama", result.name)



if __name__ == "__main__":
    unittest.main()