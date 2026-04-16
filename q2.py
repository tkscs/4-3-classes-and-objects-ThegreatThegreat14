class Cat:
    """a cat"""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} says meow!")

ella = Cat("Ella")
ella.speak()

class Dog:
    """a dog"""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} says woof!")

lila = Dog("Lila")
lila.speak()