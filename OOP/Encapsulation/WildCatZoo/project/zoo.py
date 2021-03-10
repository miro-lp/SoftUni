
class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget - price < 0:
            return "Not enough budget"
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        if worker_name not in [w.name for w in self.workers]:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove([w for w in self.workers if w.name == worker_name][0])
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        if self.__budget - sum([w.salary for w in self.workers]) < 0:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= sum([w.salary for w in self.workers])
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        if self.__budget - sum([a.get_needs() for a in self.animals]) < 0:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= sum([a.get_needs() for a in self.animals])
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        count_info = f"You have {len(self.animals)} animals"
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        lions_info = f"----- {len(lions)} Lions:"
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        tigers_info = f"----- {len(tigers)} Tigers:"
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]
        cheetahs_info = f"----- {len(cheetahs)} Cheetahs:"

        return count_info + "\n" + lions_info + "\n" + "\n".join([str(l) for l in lions]) + \
               "\n" + tigers_info + "\n" + "\n".join([str(t) for t in tigers]) + \
               "\n" + cheetahs_info + "\n" + "\n".join([str(c) for c in cheetahs])

    def workers_status(self):
        workers_info = f"You have {len(self.workers)} workers"
        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        keepers_info = f"----- {len(keepers)} Keepers:"
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        caretakers_info = f"----- {len(caretakers)} Caretakers:"
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]
        vets_info = f"----- {len(vets)} Vets:"
        return workers_info + "\n" + keepers_info + "\n" + "\n".join([str(k) for k in keepers]) \
               + "\n" + caretakers_info + "\n" + "\n".join([str(c) for c in caretakers]) \
               + "\n" + vets_info + "\n" + "\n".join([str(v) for v in vets])
