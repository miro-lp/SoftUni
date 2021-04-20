class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        if software.capacity_consumption <= self.available_capacity and software.memory_consumption <= self.available_memory:
            self.software_components.append(software)
            # self.capacity -= software.capacity_consumption
            # self.memory -= software.memory_consumption
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)


    @property
    def available_memory(self):
        return self.memory - sum([s.memory_consumption for s in self.software_components])

    @property
    def available_capacity(self):
        return self.capacity - sum([s.capacity_consumption for s in self.software_components])

