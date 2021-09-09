from Shapes.Shape import Shape


class Rectangle(Shape):
    def __init__(self, width, length, color):
        self.width = width
        self.length = length
        super().__init__(color)

    def findArea(self):
        return self.width * self.length

    def findPerimeter(self):
        return (self.width * 2) + (self.length * 2)

    def findColor(self):
        return self.color
