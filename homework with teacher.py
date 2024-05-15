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


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")

    def add_staff(self, staff):
        self.staff.append(staff)
        print(f"Сотрудник {staff.name} добавлен в зоопарк")


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

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zoo.add_staff(zoo_keeper)
zoo.add_staff(veterinarian)

animal_sound(zoo.animals)
zoo_keeper.feed_animal(mammal)
veterinarian.heal_animal(reptile)
