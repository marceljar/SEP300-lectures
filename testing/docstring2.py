class Dog:
    """
    A simple representation of a dog.

    Attributes:
        name (str): The dog's name.
        age (int): The dog's age in years.

    Methods:
        bark():
            Prints a barking sound.
        birthday():
            Increases the dog's age by one year.
    """

    def __init__(self, name: str, age: int):
        """
        Initialize a Dog with a name and age.

        Args:
            name (str): The dog's name.
            age (int): The dog's age.
        """
        self.name = name
        self.age = age

    def bark(self):
        """Print a simple barking sound."""
        print(f"{self.name} says: Woof!")

    def birthday(self):
        """Increase the dog's age by one year."""
        self.age += 1
        print(f"Happy birthday {self.name}, \
              you are now {self.age}!")

help(Dog.bark)
help(Dog)
