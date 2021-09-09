from Shapes.Shape import Shape


class Circle(Shape):
    def __init__(self, radius, color):
        self.radius = radius

        super().__init__(color)

    def findArea(self):
        return 3.14 * pow(self.radius, 2)

    def findPerimeter(self):
        return 2 * 3.14 * self.radius

    def findColor(self):
        return self.color
