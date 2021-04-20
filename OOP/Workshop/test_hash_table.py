from unittest import TestCase

from SoftUni.SoftUni.OOP.Workshop.HashTable import HashTable


class TestHashTable(TestCase):

    def setUp(self):
        self.hashtable = HashTable()

    def test_attributes(self):
        self.assertEqual(4, len(self.hashtable.keys))
        self.assertEqual(4, len(self.hashtable.value))
        self.assertEqual(4, self.hashtable.max_capacity)

    def test_add_key_exist(self):
        self.hashtable["age"] = 25
        self.hashtable["age"] = 28
        self.assertEqual(28, self.hashtable["age"])

    def test_add_keys_more_4(self):
        for i in range(5):
            self.hashtable[f"key_{i}"] = f"value_{i}"
        self.assertEqual(8, len(self.hashtable))
        self.assertEqual(5, self.hashtable.real_len)

    def test_when_collision_occurs_expected_next_index(self):
        self.hashtable["name"] = "Peter"
        self.hashtable["age"] = 25
        self.assertEqual(1, self.hashtable.keys.index("name"))
        self.assertEqual(2, self.hashtable.keys.index("age"))

    def test_get_no_kye_exist_expected_none(self):
        self.hashtable["name"] = "Peter"
        self.assertIsNone(self.hashtable.get("age"))

    def test_get_kye_exist_expected_value(self):
        self.hashtable["name"] = "Peter"
        self.assertEqual("Peter", self.hashtable.get("name"))