from Animals import Animal, Dog, Cat, Bird
# -------------------------------------------

def PrintAnimalInfo(_animal):
    _animal.PrintAnimalInfo()

if __name__ == "__main__":
    shippered = Dog("Scott", 10, "Male", "White", "Orange")
    shippered.PrintAnimalInfo()

    fluffy = Cat("Nancy Pelosi", 5, "Unknown", "Pink", "Blue")
    fluffy.PrintAnimalInfo()

    parrot  = Bird("Bobby", 12, "Female","Golden")
    parrot.PrintAnimalInfo()

