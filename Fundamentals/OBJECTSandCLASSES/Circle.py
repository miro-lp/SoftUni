class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        p = self.diameter * self.__pi
        return p

    def calculate_area(self):
        s = (self.__pi * self.diameter ** 2) / 4
        return s

    def calculate_area_of_sector(self, angle):
        self.angle = angle
        s = ((self.__pi * self.diameter ** 2) / 4) * (self.angle / 360)
        return s



circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
