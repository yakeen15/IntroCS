class Circle():
    def __init__(self, radius):
        self.radius = radius
        # your code here

    def get_radius(self):
        return self.radius
        # your code here

    def set_radius(self, radius):
        self.radius = radius
        # your code here

    def get_area(self):
        return 3.14*self.radius**2
        # your code here

    def equal(self, c):
        return c.get_radius() == self.radius
        # your code here

    def bigger(self, c):
        if self.radius > c.get_radius():
            return self
        else:
            return c
        # your code here

c1 = Circle(5)
c2 = Circle(3)
c3 = Circle(5)
print(c1.get_area())