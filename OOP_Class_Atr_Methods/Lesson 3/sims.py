import random

#HOUSE
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

#AUTO
class Auto:
    brands = {
        'BMW': {'fuel': 100, 'strength': 100, 'consumption': 6},
        'Lada': {'fuel': 50, 'strength': 40, 'consumption': 10},
        'Volvo': {'fuel': 70, 'strength': 80, 'consumption': 8},
        'Ferrari': {'fuel': 80, 'strength': 150, 'consumption': 14},
    }

    def __init__(self):
        self.brand = random.choise(list(Auto.brands))
        self.fuel = Auto.stats[self.brand]['fuel']
        self.strength = Auto.stats[self.brand]['strength']
        self.consumption = Auto.stats[self.brand]['consumption']

#DRIVE
    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('The car cannot go')
            return False

#JOB
class Job:
    stats = {
        'Java Developer': {'salary': 50, 'gladness_less': 10},
        'Python Developer': {'salary': 40, 'gladness_less': 3},
        'C++ Developer': {'salary': 45, 'gladness_less': 25},
        'Rust Developer': {'salary': 70, 'gladness_less': 1},
    }

    def __init__(self):
        self.job = random.choise(list(Job.stats))
        self.salary = Job.stats[self.job]['salary']
        self.gladness_less = Job.stats[self.job]['gladness_less']


#HUMAN
class Human:
    def __init__(
            self,
            name='Human',
            job=None,
            home=None,
            car=None
    ):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

#GET_HOME
    def get_home(self):
        self.home = House()

#GET_CAR
    def get_car(self):
        self.car = Auto()

#GET_JOB
    def get_job(self):
        if not self.car.drive():
            self.to_repair()
            return
        self.job = Job()

#EAT
    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -=5

#TO_REPAIR
    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

#WORK
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = 'fuel'
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

#SHOPPING
    def shopping(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('Bought a fuel')
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            print('Bought food')
            self.money -= 50
            self.home.food += 50
        elif manage == 'sweets':
            print('Yummy! Yummy!')
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

#CHILL
    def chill(self):
        self.gladness += 10
        self.home.mess += 5

#CLEAN_HOME
    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

#INDEXES
    def days_indexes(self, day):
        day_str = f"Today is the {day} day of {self.name}'s life"
        print(f"{day_str:=^50}", "\n")

        human_indexes = f"{self.name}'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print('money: ', self.money)
        print('satiety: ', self.satiety)
        print('gladness: ', self.gladness)

        home_indexes = 'Home indexes'
        print(f"{home_indexes:^50}", "\n")
        print('food: ', self.home.food)
        print('mess: ', self.home.mess)

        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print('fuel: ', self.car.fuel)
        print('strength: ', self.car.strength)

#IS_ALIVE
    def is_alive(self):
        if self.gladness < 0:
            print('Depression...')
        elif self.satiety < 0:
            print('Hunger death...')
        elif self.money < -500:
            print('Bankrut...')
            return False
        else:
            return True

#LIVE
    def live(self, day):
        if not self.is_alive():
            return False

        if self.home is None:
            print('Settled in the house')
            self.get_home()

        if self.car is None:
            print('Got a car')
            self.get_home()

        if self.job is None:
            print('Got a job')
            self.get_job()

        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                self.clean_home()
            else:
                self.chill()

        elif self.money < 0:
            self.work()

        elif self.car.strength < 15:
            self.to_repair()

        elif dice == 1:
            self.chill()

        elif dice == 2:
            self.work()

        elif dice == 3:
            self.clean_home()

        elif dice == 4:
            self.shopping(manage='sweets')
        return True

nick = Human(name='Nick')
for day in range(1, 365):
    if not nick.live(day):
        break
