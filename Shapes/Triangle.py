from Shapes.Shape import Shape

class Triangle(Shape):
    def __init__(self, height, base, side2, side3, color):
        self.height = height
        self.base = base
        self.side2 = side2
        self.side3 = side3

        super().__init__(color)

    def findArea(self):
        return 0.5 * self.base * self.height

    def findPerimeter(self):
        return self.base + self.side2 + self.side3

    def findColor(self):
        return self.color
