class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.dictionary) <= 0:
            raise StopIteration
        key, value = [(i, v) for i, v in self.dictionary.items()][0]
        self.dictionary.pop(key)
        return (key, value)


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
