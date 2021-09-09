from Shapes.Shape import Shape


class Square(Shape):
    def __init__(self, width,color):
        self.width = width
        super().__init__(color)

    def findArea(self):
        return self.width * self.width

    def findPerimeter(self):
        return self.width * 4

    def findColor(self):
        return self.color
