class Human:
    bio = 'HomoSapiens'

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Human):
    def __init__(self, name, age=25, degree='Bachelor', subject='CS'):
        super().__init__(name, age)
        self. degree = degree
        self.subject = subject

nick = Student(name='Nick')
print(nick.bio)
print(nick.name)
print(nick.age)
print(nick.degree)
print(nick.subject)

print("------------------------------------------------------------------")

class Dog:
    strength = 100

class Cat(Dog):
    lives = 9

class Wolf(Cat):
    aggressiveness = 30

f = Wolf()
print(f.strength)
print(f.lives)
print(f.aggressiveness)

print("------------------------------------------------------------------")

class Grandparent:

    a = 1
    d = 4

class Parent(Grandparent):

    b = 2
    d = 5

class Child(Parent):

    c = 3

x = Child()
print(x.a)
print(x.b)
print(x.c)
print(x.d)

print("------------------------------------------------------------------")



class Computer:
    memory = 120

    def __init__(self, chip):
        self.chip = chip

class Display:
    resolution = '4k'

    def __init__(self, let_type):
        self.let_type = let_type

class SmartPhone(Computer, Display):
    brand = 'Apple'

    def __init__(self, chip, let_type, carrier):
        super(Computer, self).__init__()

phone = SmartPhone()
print(phone.memory)
print(phone.resolution)
print(phone.brand)



