class CustomList:
    def __init__(self):
        self.capacity = 4
        self.v_count = 0
        self.values = [None] * self.capacity

    def __iter__(self):
        self.__grow()
        for i in range(self.v_count):
            yield self.values[i]

    def append(self, value):
        self.values[self.v_count] = value
        self.v_count += 1
        return self 

    def remove(self, index):
        pass

    def get(self, index):
        pass

    def extend(self, iterable):
        pass

    def insert(self, index, value):
        pass

    def pop(self):
        pass

    def index(self, value):
        pass

    def count(self, value):
        pass

    def reverse(self):
        pass

    def copy(self):
        pass

    def __grow(self):
        if self.v_count < self.capacity:
            return
        self.values += [None] * self.capacity
        self.capacity *= 2
