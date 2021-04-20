import unittest

from project.appliances.fridge import Fridge
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Petrovi", 600, 2)

    def test_init__expected_correct_attribute(self):
        self.assertEqual("Petrovi", self.room.family_name)
        self.assertEqual(600, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertListEqual([],self.room.children)
        self.assertEqual(0,self.room.expenses)

    def test_expenses_when_expenses_less_zero_expected_error(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -20
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_expenses_when_expenses_positive(self):
        self.room.expenses = 20
        self.assertEqual(20, self.room.expenses)

    def test_calculate_expenses_when_args_one_list(self):
        self.room.calculate_expenses([TV(),Fridge()])
        self.assertEqual(81, self.room.expenses)

    def test_calculate_expenses_when_args_zero(self):
        self.room.calculate_expenses([])
        self.assertEqual(0, self.room.expenses)

    def test_calculate_expenses_when_args_more_one_list(self):
        self.room.calculate_expenses([TV(),Fridge()],[Child(2,2,2)])
        self.assertEqual(261, self.room.expenses)


if __name__ == "__main__":
    unittest.main()