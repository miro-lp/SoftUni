import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    name = "Pesho"
    type = "human"
    sound = "Hello"

    def setUp(self):
        self.mammal = Mammal(self.name, self.type, self.sound)

    def test_mammal_init__when_correct_args__expect_initialized(self):
        self.assertEqual(self.name, self.mammal.name)
        self.assertEqual(self.type, self.mammal.type)
        self.assertEqual(self.sound, self.mammal.sound)

    def test_mammal_make_sound__when_is_called__expect_correct_str(self):
        expected_info = f"{self.name} makes {self.sound}"
        actual_info = self.mammal.make_sound()
        self.assertEqual(expected_info, actual_info)

    def test_mammal_get_kingdom__when_is_called__expect_default_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_mammal_info__when_is_called__expect_correct_str(self):
        expected_info = f"{self.name} is of type {self.type}"
        actual_info = self.mammal.info()
        self.assertEqual(expected_info, actual_info)

    def test_mammal_private_attribute__when_is_called__expect_error(self):
        with self.assertRaises(Exception):
            self.mammal.kingdom

    def test_mammal_private_attribute__is_it_private(self):
        self.assertEqual("animals", self.mammal._Mammal__kingdom)


if __name__=="__main__":
    unittest.main()
