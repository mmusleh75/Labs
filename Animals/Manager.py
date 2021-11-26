from Animals import Dog, Cat, Bird
# -------------------------------------------

def PrintAnimalInfo(_animal):
    _animal.PrintAnimalInfo()

def main():
    shippered = Dog("Scott", 10, "Male", "White", "Orange")
    shippered.PrintAnimalInfo()

    fluffy = Cat("Nancy Pelosi", 5, "Unknown", "Pink", "Blue")
    fluffy.PrintAnimalInfo()

    parrot  = Bird("Bobby", 12, "Female","Golden")
    parrot.PrintAnimalInfo()

