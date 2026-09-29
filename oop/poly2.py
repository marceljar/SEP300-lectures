class Dog:
    def make_sound(self):
        return "Woof!"


class Cat:
    def make_sound(self):
        return "Meow!"


class Alarm:
    def make_sound(self):
        return "Beep! Beep!"


def play_sound(obj):
    print(obj.make_sound())


dog = Dog()
cat = Cat()
alarm = Alarm()

play_sound(dog)
play_sound(cat)
play_sound(alarm)