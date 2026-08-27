class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):  # Overrides parent method
        print("Woof!")

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # Animal.__init__(self, name)
        self.breed = breed

    def speak(self):  # Overrides parent method
        print("Meow!")


animals = [Dog("Billy", "Husky"), Cat("Pumpkin", "Siamese"), \
           Animal("Clarabelle")]

for animal in animals:
    print(f"This animal is called {animal.name}.")
    if (hasattr(animal, "breed")):
        print(f"It is a {animal.breed}.")
    animal.speak()
