class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def __add__(self, c):
        return Circle(self.get_radius() + c.get_radius())
        # your code here

    def __str__(self):
        return str(self.get_radius())
        # your code here

c1 = Circle(1)
c2 = Circle(2)

print(str(c1+c2))