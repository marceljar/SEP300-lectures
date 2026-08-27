class Animal:
    def __init__(self):
        print("Animal constructor called")

    def speak(self):
        print("This animal makes a sound.")

class Mammal(Animal):
    def __init__(self):
        print("Mammal constructor called")
        super().__init__()

    def speak(self):
        print("This mammal makes a sound.")

class Pet(Animal):
    def __init__(self):
        print("Pet constructor called")
        super().__init__()

    def speak(self):
        print("This pet makes a sound.")

class Dog(Mammal, Pet):
    def __init__(self):
        print("Dog constructor called")
        super().__init__()
    
    # def speak(self):
    #     print("Woof!")

dog = Dog()
dog.speak()
