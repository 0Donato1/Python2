class Human:
    def __init__(self, name='Human'):
        self.name = name



class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers += human

    def print_passenger(self):
        names = [p.name for p in self.passengers]
        print(names)


nick = Human(name='Nick')
kate = Human(name='Kate')
car = Auto(brand="Chevrolet")

car.add_passengers([nick, kate])
car.print_passenger()



