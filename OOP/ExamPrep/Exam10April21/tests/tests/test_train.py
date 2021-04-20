import unittest

from project.train.train import Train


class TestTrain(unittest.TestCase):
    def setUp(self):
        self.train = Train("Express", 5)

    def test_init__when_initialized__correct_attribute(self):
        self.assertEqual("Express", self.train.name)
        self.assertEqual(5,self.train.capacity)
        self.assertEqual(0,len(self.train.passengers))
        self.assertListEqual([],self.train.passengers)

    def test_add__when_name_not_in_list__expected_add(self):
        result = self.train.add("Pesho")
        self.assertEqual("Added passenger Pesho",result)
        self.assertEqual(1,len(self.train.passengers))

    def test_add__when_name_in_list__expected_error(self):
        self.train.add("Pesho")
        with self.assertRaises(ValueError) as ex:
            self.train.add("Pesho")
        self.assertEqual("Passenger Pesho Exists", str(ex.exception))

    def test_add__when_is_full__expected_error(self):
        for i in range(5):
            self.train.add(f"Pesho{i}")
        with self.assertRaises(ValueError) as ex:
            self.train.add("Pesho")
        self.assertEqual("Train is full", str(ex.exception))

    def test_remove__if_name_not_in_list__expected_error(self):
        with self.assertRaises(ValueError) as ex:
            self.train.remove("Pesho")
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove__if_name_exist__expected_remove(self):
        self.train.add("Pesho")
        result = self.train.remove("Pesho")
        self.assertEqual("Removed Pesho", result)
        self.assertEqual(0, len(self.train.passengers))

if __name__ == "__main__":
    unittest.main()