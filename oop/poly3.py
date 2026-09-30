class Animal:
    def __init__(self, name):
        self.name = name # attribute used by child classes

    def speak(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def speak(self):  # Overrides parent method
        print("Woof!")

class Cat(Animal):
    def speak(self):  # Overrides parent method
        print("Meow!")


class Tree():
    def __init__(self, name):
            self.name = name

    def speak(self):
        print("Trees don´t talk, silly!")


animals = [Dog("Billy"), Cat("Pip"), Animal("Clara"), Tree("Oaky")]

for animal in animals:
    print(f"This animal is called {animal.name}.")
    animal.speak()
