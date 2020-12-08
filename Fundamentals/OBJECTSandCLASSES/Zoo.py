class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        if species == "bird":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        zoo_name = self.name
        if species == "mammal":
            species_names = self.mammals
        elif species == "fish":
            species_names = self.fishes
        elif species == "bird":
            species_names = self.birds
        names = ", ".join(species_names)
        return f"{species} in {zoo_name}: {names}"
    def get_all_animals(self):
        return self.__animals


zoo_name = input()

zoo = Zoo(zoo_name)
n = int(input())

for i in range(n):
    animal = list(input().split(" "))
    zoo.add_animal(animal[0], animal[1])

species = input()

print(zoo.get_info(species))
print(f"Total animals: {zoo.get_all_animals()}")
