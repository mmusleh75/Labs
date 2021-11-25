class Animal(object):
    def __init__(self, name):
        self.name = name



class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "raf raf"

    def getName(self):
        return self.name

class Bird(Animal):
    def speak(self):
        return "tweet"

class Cat(Animal):
    def speak(self):
        return "Meiao"

d = Dog("Scott")
print(d.speak())
print(d.getName())
exit(1)
b = Bird("Duck")
print(b.speak())
print(b.getName())
