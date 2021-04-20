import unittest

from project.hardware.hardware import Hardware
from project.software.light_software import LightSoftware


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware("Test", "Light", 100, 200)

    def test_init__expected_attribute(self):
        self.assertEqual("Test", self.hardware.name)
        self.assertEqual("Light", self.hardware.type)
        self.assertEqual(100, self.hardware.capacity)
        self.assertEqual(200, self.hardware.memory)
        self.assertEqual(0, len(self.hardware.software_components))

    def test_install__when_software_more_capacity_expected_error(self):
        soft = LightSoftware("Program", 300, 100)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(soft)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_install__when_software_more_memory_expected_error(self):
        soft = LightSoftware("Program", 10, 500)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(soft)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_install__when_software_is_installed(self):
        soft = LightSoftware("Program", 50, 100)
        self.hardware.install(soft)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_uninstall__when_software_is_uninstalled(self):
        soft = LightSoftware("Program", 50, 100)
        self.hardware.install(soft)
        self.hardware.uninstall(soft)
        self.assertEqual(0, len(self.hardware.software_components))

    def test_uninstall__when_software_not_exist_isnt_uninstalled(self):
        soft = LightSoftware("Program", 50, 100)
        soft_1 = LightSoftware("Program_1", 60, 180)
        self.hardware.install(soft)
        self.hardware.uninstall(soft_1)
        self.assertEqual(1, len(self.hardware.software_components))

if __name__ == "__main__":
    unittest.main()
