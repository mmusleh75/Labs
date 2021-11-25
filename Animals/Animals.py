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

        if type(self) == Dog:
            print("Since I'm a dog, my saliva color is",self.SalivaColor())

        print("-------------------------")

class Cat(Animal):

    def Move(self):
        return "hey I'm cat moving my cat way"

    def MakeSound(self):
        return "Meow"

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

class Bird(Animal):

    def Move(self):
        return "hey I'm bird moving my bird way"

    def MakeSound(self):
        return "Tweet"

# -------------------------------------------

def PrintAnimalInfo(_animal):
    _animal.PrintAnimalInfo()

if __name__ == "__main__":
    shippered = Dog("Scott", 10, "Male", "White", "Orange")
    PrintAnimalInfo(shippered)

    fluffy = Cat("Nancy Pelosi", 5, "Unknown", "Pink")
    PrintAnimalInfo(fluffy)

    Parrot  = Bird("Bobby", 12, "Female","Golden")
    PrintAnimalInfo(Parrot)





