class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 0:
            raise StopIteration
        current_index = self.index
        self.index += 1
        self.number -= 1
        if current_index >= len(self.sequence):
            current_index = 0
            self.index = 1
        return self.sequence[current_index]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
