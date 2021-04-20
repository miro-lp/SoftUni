import unittest

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        self.players = PlayerRepository()


    def test_init__count__list(self):
        self.assertEqual(0, len(self.players.players))
        self.assertEqual(0, self.players.v_count)

    def test_add_player_when_doesnt_exist(self):
        player_1 = Beginner("Pesho")
        self.players.add(player_1)
        self.assertEqual(1, len(self.players.players))
        self.assertEqual(1, self.players.v_count)

    def test_add_player_when_exist(self):
        player_1 = Beginner("Pesho")
        self.players.add(player_1)
        with self.assertRaises(ValueError) as ex:
            self.players.add(player_1)
        self.assertEqual("Player Pesho already exists!", str(ex.exception))
        self.assertEqual(1, len(self.players.players))
        self.assertEqual(1, self.players.v_count)

    def test_remove_when_empty_str(self):
        with self.assertRaises(ValueError) as ex:
            self.players.remove("")
        self.assertEqual("Player cannot be an empty string!", str(ex.exception))

    def test_remove_when_has_str(self):
        player_1 = Beginner("Pesho")
        self.players.add(player_1)
        self.players.remove("Pesho")
        self.assertEqual(0, len(self.players.players))
        self.assertEqual(0, self.players.v_count)

    def test_find(self):
        player_1 = Beginner("Pesho")
        self.players.add(player_1)
        result = self.players.find("Pesho")
        self.assertEqual("Pesho", result.username)



if __name__ == "__main__":
    unittest.main()