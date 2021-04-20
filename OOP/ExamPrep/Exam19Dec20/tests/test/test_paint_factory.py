import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.factory = PaintFactory("PHP", 250)

    def test_init__when_initialize__expect_attributes(self):
        self.assertEqual("PHP", self.factory.name)
        self.assertEqual(250, self.factory.capacity)
        # self.assertListEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)
        self.assertEqual(0, len(self.factory.ingredients))
        self.assertDictEqual({}, self.factory.products)

    def test_add_ingredient__when_not_valid__expected_error(self):
        with self.assertRaises(TypeError) as ex:
            self.factory.add_ingredient("black", 50)
        self.assertEqual("Ingredient of type black not allowed in PaintFactory", str(ex.exception))

    def test_add_ingredient__when_no_capacity__expected_error(self):
        with self.assertRaises(ValueError) as ex:
            self.factory.add_ingredient("white", 500)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingredient__when_valid__expected_new_value_in_dict(self):
        self.factory.add_ingredient("white", 50)
        self.assertDictEqual({"white": 50}, self.factory.ingredients)
        self.assertEqual(1, len(self.factory.ingredients))

    def test_add_ingredient__when_exist__expected_value_increase(self):
        self.factory.add_ingredient("white", 50)
        self.factory.add_ingredient("white", 50)
        self.assertEqual(100, self.factory.ingredients["white"])
        self.assertEqual(1, len(self.factory.ingredients))

    # def test_add_ingredient__when_capacity_is_less__expected_error(self):
    #     self.factory.add_ingredient("white", 100)
    #     self.factory.add_ingredient("yellow", 100)
    #     with self.assertRaises(ValueError) as ex:
    #         self.factory.add_ingredient("white", 100)
    #     self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_remove_ingredient__when_unvalid_key__expected_error(self):
        self.factory.add_ingredient("white", 50)
        with self.assertRaises(KeyError) as ex:
            self.factory.remove_ingredient("black", 50)
        # self.assertEqual("'No such product in the factory'", str(ex.exception))

    def test_remove_ingredient__when_unvalid_quantity__expected_error(self):
        self.factory.add_ingredient("white", 50)
        with self.assertRaises(ValueError) as ex:
            self.factory.remove_ingredient("white", 100)
        self.assertEqual("Ingredient quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient__when_value_equal_quantity__expected_zero(self):
        self.factory.add_ingredient("white", 50)
        self.factory.remove_ingredient("white", 50)
        self.assertEqual(0, self.factory.ingredients["white"])
        self.assertEqual(1, len(self.factory.ingredients))

    def test_remove_ingredient__when_valid_quantity__expected_reduce_quantity(self):
        self.factory.add_ingredient("white", 50)
        self.factory.remove_ingredient("white", 20)
        self.assertEqual(30, self.factory.ingredients["white"])
        self.assertDictEqual({"white": 30}, self.factory.ingredients)

    def test_can_add__when_value_mare_capacity__expected_false(self):
        self.factory.add_ingredient("white", 200)
        result = self.factory.can_add(100)
        self.assertFalse(result)

    def test_can_add__when_value_mare_capacity__expected_true(self):
        self.factory.add_ingredient("white", 50)
        result = self.factory.can_add(100)
        self.assertTrue(result)

    def test_check_object_inherit_factory(self):
        self.assertEqual("Factory", self.factory.__class__.__base__.__name__)


if __name__ == "__main__":
    unittest.main()
