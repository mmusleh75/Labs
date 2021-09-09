from Shapes.Square import Square
from Shapes.Triangle import Triangle
from Shapes.Circle import Circle
from Shapes.Rectangle import Rectangle

s = Square(9,"green")
c = Circle(5, "red")
r = Rectangle(3,4,"black")
t = Triangle(5,5,3,4,"yellow")

print("Square")
print("Area:", s.findArea())
print("Perimeter:", s.findPerimeter())
print("Color:", s.findColor())

print("Circle")
print("Area:", c.findArea())
print("Perimeter:", c.findPerimeter())
print("Color:", c.findColor())

print("Rectangle")
print("Area:", r.findArea())
print("Perimeter:", r.findPerimeter())
print("Color:", r.findColor())

print("Triangle")
print("Area:", t.findArea())
print("Perimeter:", t.findPerimeter())
print("Color:", t.findColor())
