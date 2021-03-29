import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    username = "Pikacho"
    health = 15
    damage = 10.5
    level = 2

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_hero_init__when_is_called__expected_attribute(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_hero_battle__called_same_username__expected_error(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_battle__called_health_less_zero__expected_error(self):
        self.hero.health = 0
        enemy = Hero("Pesho", 3, 20.5, 5.2)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_hero_battle__called_health_enemy_less_zero__expected_error(self):
        enemy = Hero("Pesho", 3, 0, 5.2)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Pesho. He needs to rest", str(ex.exception))

    def test_hero_battle__called_both_health_less_zero__expected_draw(self):
        enemy = Hero("Pesho", 3, 3, 5.2)
        result = self.hero.battle(enemy)
        self.assertEqual("Draw", result)

    def test_hero_battle__called_enemy_health_less_zero__expected_win(self):
        enemy = Hero("Pesho", 3, 3, 3.2)
        result = self.hero.battle(enemy)
        self.assertEqual("You win", result)
        self.assertEqual(self.level + 1, self.hero.level)
        self.assertEqual(self.health - 3 * 3.2 + 5, self.hero.health)
        self.assertEqual(self.damage + 5, self.hero.damage)

    def test_hero_battle__called_player_health_less_zero__expected_lose(self):
        enemy = Hero("Pesho", 3, 30, 6.2)
        result = self.hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(4, enemy.level)
        self.assertEqual(30 + 5 - 10.5 * 2, enemy.health)
        self.assertEqual(11.2, enemy.damage)

    def test_hero_str__called__expected_correct_str(self):
        expected = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"
        self.assertEqual(expected,self.hero.__str__())


if __name__ == "__main__":
    unittest.main()
