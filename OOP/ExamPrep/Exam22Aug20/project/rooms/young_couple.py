from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    room_cost = 20
    default_room_count = 2
    appliances = [TV(),TV(), Fridge(), Fridge(), Laptop(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one + salary_two, self.default_room_count)
        self.calculate_expenses(self.appliances)
