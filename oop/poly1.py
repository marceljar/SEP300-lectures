class Dog:
    def speak(self):
        print("Woof!")


class Person:
    def speak(self):
        print("Hello!")


class Alarm:
    def speak(self):
        print("Beep! Beep!")


class Robot:
    def speak(self):
        print("Greetings, human.")


objects = [
    Dog(),
    Person(),
    Alarm(),
    Robot()
]


for obj in objects:
    obj.speak()