x = 10

def Cube(width, height, length, x):
    print(x)
    cube_value = width * height * length
    area_value = width * length
    return cube_value, area_value

def func(x):
    print(x)
    x = 30
    print(x)

print(x)

cube_value, area_value = Cube(10,10,10, x)

print(cube_value, area_value)

print(x)

func(x)
