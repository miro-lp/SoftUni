import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    fuel = 25.3
    capacity = 25.3
    horse_power = 85.5
    fuel_consumption = 1.25

    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_vehicle_init__when_correct_args__expect_initialized(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.capacity, self.vehicle.capacity)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_vehicle_drive__when_fuel_for_give_km_is_more__expected_error(self):
        with self.assertRaises(Exception) as content:
            self.vehicle.drive(50)
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(content.exception))

    def test_vehicle_drive__when_fuel_for_give_km_is_less__expected_less_fuel(self):
        self.vehicle.drive(5)
        self.fuel -= self.fuel_consumption * 5
        self.assertEqual(self.fuel, self.vehicle.fuel)

    def test_vehicle_refuel__fuel_is_more_capacity__expected_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)
        self.assertEqual("Too much fuel", str(ex.exception))
        self.assertEqual(self.fuel, self.vehicle.fuel)

    def test_vehicle_refuel__fuel_is_less_capacity__expected_refuel(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(10)
        self.fuel -= self.fuel_consumption * 10
        self.fuel += 10
        self.assertEqual(self.fuel, self.vehicle.fuel)

    def test_vehicle_str__called__expected_correct_str(self):
        vehicle_str_expected = f"The vehicle has {self.horse_power} " \
                               f"horse power with {self.fuel} fuel left and {self.fuel_consumption} fuel consumption"
        self.assertEqual(vehicle_str_expected, self.vehicle.__str__())


if __name__ == "__main__":
    unittest.main()
