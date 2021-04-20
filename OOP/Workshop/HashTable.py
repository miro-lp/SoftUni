class HashTable:
    def __init__(self):
        self.max_capacity = 4
        self.__keys = [None] * self.max_capacity
        self.__value = [None] * self.max_capacity

    def __getitem__(self, key):
        index = self.__keys.index(key)
        return self.__value[index]

    def __setitem__(self, key, value):
        if key in self.__keys:
            self.__value[self.__keys.index(key)] = value
            return
        if self.real_len == self.max_capacity:
            self.resize()
        index = self.hash(key)
        self.__keys[index] = key
        self.__value[index] = value

    def __len__(self):
        return len(self.__keys)

    def check_available_index(self, index):
        if index == len(self.__keys):
            return self.check_available_index(0)
        if self.__keys[index] is None:
            return index
        return self.check_available_index(index + 1)

    def hash(self, key):
        index = sum([ord(char) for char in key]) % self.max_capacity
        return self.check_available_index(index)

    def add(self, key, value):
        self[key] = value

    @property
    def keys(self):
        return self.__keys

    @property
    def value(self):
        return self.__value

    @property
    def real_len(self):
        return len([key for key in self.__keys if key != None])

    def resize(self):
        self.__keys = self.__keys + [None] * self.max_capacity
        self.__value = self.__value + [None] * self.max_capacity
        self.max_capacity *= 2

    def get(self, key):
        try:
            index = self.__keys.index(key)
            return self.__value[index]
        except ValueError:
            return None

#
# table = HashTable()
# table["name"] = "Peter"
# table["age"] = 25
# table.add("jyv", 3)
# table["age"] = 28
#
# print(table)
# print(table.get("name"))
# print(table["age"])
# print(table.get("jyv"))
# print(len(table))
