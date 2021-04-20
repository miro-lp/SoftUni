from project.supply.food_supply import FoodSupply
from project.survivor import Survivor
from project.supply.water_supply import WaterSupply
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        if len([s for s in self.supplies if s.__class__.__name__ == "FoodSupply"]) == 0:
            raise IndexError("There are no food supplies left!")
        return [s for s in self.supplies if s.__class__.__name__ == "FoodSupply"]

    @property
    def water(self):
        if len([s for s in self.supplies if s.__class__.__name__ == "WaterSupply"]) == 0:
            raise IndexError("There are no water supplies left!")
        return [s for s in self.supplies if s.__class__.__name__ == "WaterSupply"]

    @property
    def painkillers(self):
        if len([s for s in self.medicine if s.__class__.__name__ == "Painkiller"]) == 0:
            raise IndexError("There are no painkillers left!")
        return [s for s in self.medicine if s.__class__.__name__ == "Painkiller"]

    @property
    def salves(self):
        if len([s for s in self.medicine if s.__class__.__name__ == "Salves"]) == 0:
            raise IndexError("There are no salves left!")
        return [s for s in self.medicine if s.__class__.__name__ == "Salves"]

    def add_survivor(self, survivor):
        if survivor.name in [s.name for s in self.survivors]:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type: str):
        if survivor.needs_healing:
            for med in self.medicine[::-1]:
                if med.__class__.__name__ == medicine_type:
                    self.medicine.remove(med)
                    med.apply(survivor)
                    return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            for sust in self.supplies[::-1]:
                if sust.__class__.__name__ == sustenance_type:
                    self.supplies.remove(sust)
                    sust.apply(survivor)
                    return f"{survivor.name} healed successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age * 2
        for s in self.survivors:
            self.sustain(s, "FoodSupply")
            self.sustain(s, "WaterSupply")


survivor_1 = Survivor("Pesho", 20)
survivor_2 = Survivor("Gosho", 22)
survivor_3 = Survivor("Mimi", 19)
water = WaterSupply()
food = FoodSupply()
pain = Painkiller()
salve = Salve()
bunker = Bunker()
bunker.add_survivor(survivor_1)
bunker.add_survivor(survivor_2)
bunker.add_survivor(survivor_3)

bunker.add_medicine(pain)
bunker.add_medicine(salve)
bunker.add_supply(water)
bunker.add_supply(food)
bunker.add_medicine(pain)
bunker.add_medicine(salve)
bunker.add_supply(water)
bunker.add_supply(food)
print(survivor_1.needs)
print(survivor_1.needs_healing)
print(bunker.supplies)
survivor_1.health = 40
survivor_1.needs = 40
food.apply(survivor_1)
print(survivor_1.needs)
pain.apply(survivor_1)
print(bunker.heal(survivor_1, "Salve"))
print(survivor_1.health)
print(bunker.medicine)
print(bunker.painkillers)
bunker.next_day()
print(survivor_1.needs)
print(survivor_2.needs)
print(survivor_3.needs)