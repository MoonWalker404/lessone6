class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print("Чирик")

class Mammal(Animal):
    def make_sound(self):
        print("Му")

class Reptile(Animal):
    def make_sound(self):
        print("Шшш")

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)


    def add_staff(self, staff):
        self.staff.append(staff)


class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

bird = Bird("Голубь", 2)
mammal = Mammal("Корова", 5)
reptile = Reptile("Змея", 3)

zoo = Zoo()
zoo_keeper = ZooKeeper("Гоша")
veterinarian = Veterinarian("Доктор Петров")

zoo.add_animal([bird, mammal, reptile])
zoo.add_staff([zoo_keeper, veterinarian])

for animal in zoo.animals:
    animal.make_sound()

for staff in zoo.staff:
    if isinstance(staff, ZooKeeper):
        staff.feed_animal(zoo.animals[0])
    elif isinstance(staff, Veterinarian):
        staff.heal_animal(zoo.animals[1])

