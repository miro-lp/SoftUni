import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def setUp(self):
        self.player_1 = Beginner("Pesho")
        self.player_2 = Advanced("Gosho")
        self.card_1 = MagicCard("Dama")
        self.card_2 = TrapCard("King")
        self.player_1.card_repository.add(self.card_2)
        self.player_2.card_repository.add(self.card_1)

    def test_fight_when_player_is_dead(self):
        self.player_2.is_dead = True
        with self.assertRaises(ValueError) as ex:
            BattleField.fight(self.player_1, self.player_2)
        self.assertEqual("Player is dead!", str(ex.exception))

    def test_fight_when_one_player_is_beginner(self):
        BattleField.fight(self.player_1, self.player_2)
        self.assertEqual(90, self.player_1.health)
        self.assertEqual(180, self.player_2.health)

    def test_fight_when_attacker_is_dead_after_battle(self):
        self.player_2.card_repository.add(self.card_2)
        BattleField.fight(self.player_1, self.player_2)
        self.assertTrue(self.player_1.is_dead)
        self.assertEqual(185, self.player_2.health)

    def test_fight_when_enemy_is_dead_after_battle(self):
        card_3 = TrapCard("Vale")
        self.player_1.card_repository.add(card_3)
        self.player_1.card_repository.add(self.card_1)
        BattleField.fight(self.player_1, self.player_2)
        self.assertTrue(self.player_2.is_dead)
        self.assertEqual(180, self.player_1.health)


if __name__ == "__main__":
    unittest.main()