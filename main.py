class Engine():
    def start(self):
        print(f"Двигатель запущен")

    def stop(self):
        print(f"Двигатель остановлен")

class Car():
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

my_car = Car()
my_car.start()
my_car.stop()
print("\n")


class Teacher():
    def teach(self):
        print("Преподователь учит")

class School():
    def __init__(self, new_teacher):
        self.teacher = new_teacher

    def start_lessone(self):
        self.teacher.teach()
        print("Урок начинается")

my_teacher = Teacher()
my_school = School(my_teacher)
my_teacher.teach()
my_school.start_lessone()
print("\n")


class Dog():
    def speek(self):
        return "Woof!"

class Cat():
    def speek(self):
        return "Meow!"

def a(animal):
    print(animal.speek)

d = Dog()
c = Cat()

a(d)
a(c)