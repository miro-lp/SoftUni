import unittest

from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    def setUp(self):
        self.card = TrapCard("Dama")

    def test_init_name_damage_health(self):
        self.assertEqual(120, self.card.damage_points)
        self.assertEqual(5, self.card.health_points)
        self.assertEqual("Dama", self.card.name)

    def test_init_empty_str_name(self):
        with self.assertRaises(ValueError) as ex:
            card_1 = TrapCard("")
        self.assertEqual("Card's name cannot be an empty string.",str(ex.exception))

    def test_class_parent_name(self):
        self.assertEqual("Card", self.card.__class__.__base__.__name__)

if __name__ == "__main__":
    unittest.main()