import unittest

from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):
    def setUp(self):
        self.player = Advanced("Pesho")

    def test_init_name(self):
        self.assertEqual("Pesho",self.player.username)

    def test_initial_health(self):
        self.assertEqual(250, self.player.health)

    def test_class_parent_name(self):
        self.assertEqual("Player", self.player.__class__.__base__.__name__)

    def test_take_damage__when_is_less_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.player.take_damage(-6)
        self.assertEqual("Damage points cannot be less than zero.", str(ex.exception))

    def test_take_damage__when_health_bigger_damage(self):
        self.player.take_damage(50)
        self.assertEqual(200, self.player.health)

    def test_take_damage__when_health_less_damage(self):
        self.player.take_damage(251)
        self.assertTrue(self.player.is_dead)

if __name__ == "__main__":
    unittest.main()
