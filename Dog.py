class Dog:
    species = "Canis Familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old!"

    def speak(self, sound):
        return f"{self.name} barks {sound}"

class BullDog(Dog):
    def speak(self, sound="yo Dog"):
        return super().speak(sound)

class Shippered(Dog):
    def speak(self, sound="sheap Dog"):
        return super().speak(sound)
