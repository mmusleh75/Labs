class Animal:
    def __init__(self, _name, _age, _gender, _color):
        self.name = _name
        self.age = _age
        self.gender = _gender
        self.color = _color

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def getColor(self):
        return self.color

    def PrintAnimalInfo(self):
        print(self.name, self.age, self.gender, self.color)
        print(self.Move())
        print("I make a",self.MakeSound(), "sound")
        print(self.EatFood())

        if type(self) == Dog:
            print("Since I'm a dog, my saliva color is",self.SalivaColor())

        if type(self) == Cat:
            print("Since I'm a cat, my eye colors are", self.EyeColor())

        print("-------------------------")

class Cat(Animal):
    def __init__(self, _name, _age, _gender, _color, _eyeColor):
        super().__init__(_name, _age, _gender, _color)
        self.eyeColor = _eyeColor

    def Move(self):
        return "hey I'm cat moving my cat way"

    def MakeSound(self):
        return "Meow"

    def EatFood(self):
        return "I'm a can, I eat cat food"

    def EyeColor(self):
        return self.eyeColor

class Dog(Animal):
    def __init__(self, _name, _age, _gender, _color, _salivaColor):
        super().__init__(_name, _age, _gender, _color)
        self.salivaColor = _salivaColor

    def Move(self):
        return "hey I'm dog moving my dog way"

    def MakeSound(self):
        return "Ruff"

    def SalivaColor(self):
        return self.salivaColor

    def EatFood(self):
        return "I'm a dog, I eat bones"

class Bird(Animal):

    def Move(self):
        return "hey I'm bird moving my bird way"

    def MakeSound(self):
        return "Tweet"

    def EatFood(self):
        return "I'm a bird, I eat seeds"




