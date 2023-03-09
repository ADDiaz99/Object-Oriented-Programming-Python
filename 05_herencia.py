class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed

    def make_sound(self):
        print("Meow!")

my_dog = Dog("Fido", "Golden Retriever")
my_cat = Cat("Fluffy", "Persian")

print(f"{my_dog.name} is a {my_dog.species} ({my_dog.breed})")
my_dog.make_sound()

print(f"{my_cat.name} is a {my_cat.species} ({my_cat.breed})")
my_cat.make_sound()