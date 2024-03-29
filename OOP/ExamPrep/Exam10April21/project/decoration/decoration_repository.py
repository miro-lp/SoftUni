class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration not in self.decorations:
            return False
        self.decorations.remove(decoration)
        return True

    def find_by_type(self, decoration_type: str):
        find_decoration = [d for d in self.decorations if d.__class__.__name__ == decoration_type]
        if len(find_decoration) > 0:
            return find_decoration[0]


