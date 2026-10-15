class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")

    def sniff(self, other_dog):
        print(f"{self.name} is sniffing {other_dog.name}.")

Billy = Dog("Billy")
print("My dog's name is:", Billy.name)
Billy.bark()

Coco = Dog("Coco")
print("My dog's name is:", Coco.name)
Coco.bark()

Billy.sniff(Coco)
