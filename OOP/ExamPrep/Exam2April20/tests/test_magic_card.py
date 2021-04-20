import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def setUp(self):
        self.card = MagicCard("Dama")

    def test_init_name_damage_health(self):
        self.assertEqual(5, self.card.damage_points)
        self.assertEqual(80, self.card.health_points)
        self.assertEqual("Dama", self.card.name)

    def test_init_empty_str_name(self):
        with self.assertRaises(ValueError) as ex:
            card_1 = MagicCard("")
        self.assertEqual("Card's name cannot be an empty string.",str(ex.exception))

    def test_class_parent_name(self):
        self.assertEqual("Card", self.card.__class__.__base__.__name__)


if __name__ == "__main__":
    unittest.main()