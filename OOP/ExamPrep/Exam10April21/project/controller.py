from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "SaltwaterAquarium":
            aquarium = SaltwaterAquarium(aquarium_name)
            self.aquariums.append(aquarium)
        elif aquarium_type == "FreshwaterAquarium":
            aquarium = FreshwaterAquarium(aquarium_name)
            self.aquariums.append(aquarium)
        else:
            return "Invalid aquarium type."
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            decoration = Ornament()
            self.decorations_repository.add(decoration)
        elif decoration_type == "Plant":
            decoration = Plant()
            self.decorations_repository.add(decoration)
        else:
            return "Invalid decoration type."
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        if aquarium_name in [a.name for a in self.aquariums]:
            if self.decorations_repository.find_by_type(decoration_type):
                aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
                decoration = self.decorations_repository.find_by_type(decoration_type)
                aquarium.add_decoration(decoration)
                self.decorations_repository.remove(decoration)
                return f"Successfully added {decoration_type} to {aquarium_name}."
            else:
                return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type == "FreshwaterFish":
            new_fish = FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == "SaltwaterFish":
            new_fish = SaltwaterFish(fish_name, fish_species, price)
        else:
            return f"There isn't a fish of type {fish_type}."
        if len([a for a in self.aquariums if a.name == aquarium_name]) > 0:
            aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
            return aquarium.add_fish(new_fish)

    def feed_fish(self, aquarium_name: str):
        if len([a for a in self.aquariums if a.name == aquarium_name]) > 0:
            aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
            aquarium.feed()
            return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        if len([a for a in self.aquariums if a.name == aquarium_name]) > 0:
            aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
            value = 0
            for f in aquarium.fish:
                value += f.price
            for d in aquarium.decorations:
                value += d.price
            return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        return "\n".join([str(a) for a in self.aquariums])

controller = Controller()
saltfish = SaltwaterFish("akula_1", "morski", 225.5)
print(controller.add_aquarium("SaltwaterAquarium","Morski"))
print(controller.add_aquarium("FreshwaterAquarium","Sladkovodem"))
print(controller.add_aquarium("FreshwaterAquarium","Sladkovoden2"))
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Ornament"))
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Ornament"))
print(controller.insert_decoration("Morski","Ornament"))
print(controller.insert_decoration("Sladkovodem","Plant"))
print(controller.add_fish("Morski","SaltwaterFish","akula", "morski", 225.5))
print(controller.add_fish("Sladkovodem","FreshwaterFish","beta", "rezbarovi", 12.5))
print(controller.add_fish("Sladkovodem","FreshwaterFish","beta2", "rezbarovi", 10.5))
print(controller.feed_fish("Morski"))
print(controller.feed_fish("Sladkovodem"))
print(controller.aquariums[0].add_fish(saltfish))
print(controller.aquariums[0].remove_fish(saltfish))
print(controller.aquariums[0].remove_fish(saltfish))
print(controller.calculate_value("Morski"))

print(controller.calculate_value("Sladkovodem"))
print(controller.report())
print(controller.decorations_repository.find_by_type("Ornament"))