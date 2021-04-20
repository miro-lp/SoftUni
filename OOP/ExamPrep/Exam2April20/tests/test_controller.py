import unittest


from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.controller import Controller
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()
        self.card_1 = MagicCard("Dama_1")
        self.card_2 = MagicCard("Dama")
        self.controller.card_repository.add(self.card_1)
        self.controller.card_repository.add(self.card_2)
        self.player_1 = Advanced("Gosho")
        self.player_1.card_repository.add(self.card_1)
        self.controller.player_repository.add(self.player_1)

    def test_add_player(self):
        result = self.controller.add_player("Beginner", "Pesho")
        self.assertEqual("Successfully added player of type Beginner with username: Pesho", result)
        self.assertEqual(2, len(self.controller.player_repository.players))

    def test_add_card(self):
        result = self.controller.add_card("Trap", "Thief")
        self.assertEqual("Successfully added card of type TrapCard with name: Thief", result)
        self.assertEqual(3, len(self.controller.card_repository.cards))

    def test_add_player_card(self):
        result = self.controller.add_player_card("Gosho", "Dama")
        self.assertEqual("Successfully added card: Dama to user: Gosho", result)
        for p in self.controller.player_repository.players:
            if p.username == "Gosho":
                self.assertEqual(2, len(p.card_repository.cards))

    def test_fight(self):
        player_1 = Beginner("Pesho")
        player_2 = Advanced("Gosho_1")
        card_1 = MagicCard("Dama")
        card_2 = TrapCard("King")
        player_1.card_repository.add(card_2)
        player_2.card_repository.add(card_1)
        self.controller.player_repository.add(player_1)
        self.controller.player_repository.add(player_2)
        result = self.controller.fight("Pesho", "Gosho_1")
        self.assertEqual("Attack user health 90 - Enemy user health 180", result)

    def test_report(self):
        result = self.controller.report()
        expected = "Username: Gosho - Health: 250 - Cards 1" + "\n" + "### Card: Dama_1 - Damage: 5" + "\n"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
