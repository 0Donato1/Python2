class Student:

    def __init__(self, name:str, age:float, group:str, earning:float):
        self.Name = name
        self.Age = age
        self.Group = group
        self.Earning = earning

    def ShowInfo(self):
        print(f"Name:\t{self.Name}\n"
              f"Age: \t{self.Age}\n"
              f"Group:\t{self.Group}\n"
              f"Money:\t{self.Earning}$")


    def Work(self):
        month = 0
        while month != 12:
            day = 0
            while day != 30:
                day += 1
            else:
                self.Earning += 1000
                day -= 30
                month += 1
                print("----------------------------------------------")
                print(f"Now is {month} month\n"
                      f"Your sallary for this month: \t1000$\n"
                      f"Your bugget:\t{self.Earning}$")

            if month == 1:
                self.Earning -= 250
                print(f"You pay for your apartments: \t250$\n"
                      f"Now your bugget:\t{self.Earning}$")

            if month == 2:
                self.Earning += 500
                print(f"You had a birthday, your friends presented to you: \t500$\n"
                      f"Now your bugget:\t{self.Earning}$ ")
                self.Earning -= 250
                print(f"You pay for your apartments: \t250$\n"
                      f"Now your bugget:\t{self.Earning}$")

            if month == 3:
                self.Earning -= 300
                print(f"In this month was International Womens's Day, you bought gifts worth: \t300$\n"
                      f"Now your bugget:\t{self.Earning}$ ")
                self.Earning -= 250
                print(f"You pay for your apartments: \t250$\n"
                      f"Now your bugget:\t{self.Earning}$")

            if month == 4:
                self.Earning -= 250
                print(f"You pay for your apartments: \t250$\n"
                      f"Now your bugget:\t{self.Earning}$")

            if month == 5:
                self.Earning -= 250
                print(f"You pay for your apartments: \t250$\n"
                      f"Now your bugget:\t{self.Earning}$")

            if month == 6:
                self.Earning -= 500
                print(f"Your mum and dad had a birthday: \t500$\n"
                      f"Now your bugget:\t{self.Earning}$ ")

            if month == 7:
                self.Earning -= 250
                print(f"You pay for your apartments: \t250$\n"
                      f"Now your bugget:\t{self.Earning}$")

            if month == 8:
                self.Earning -= 1500
                print(f"Your holidays cost you: \t1500$\n"
                      f"Now your bugget:\t{self.Earning}$ ")

            if month == 9:
                self.Earning -= 250
                print(f"You pay for your apartments: \t250$\n"
                      f"Now your bugget:\t{self.Earning}$")

            if month == 10:
                self.Earning -= 250
                print(f"You pay for your apartments: \t250$\n"
                      f"Now your bugget:\t{self.Earning}$")

            if month == 11:
                self.Earning -= 250
                print(f"You pay for your apartments: \t250$\n"
                      f"Now your bugget:\t{self.Earning}$")

            if month == 12:
                self.Earning -= 1000
                print(f"You bought presents for you family and friends it cost you: \t1000$\n"
                      f"Now your bugget:\t{self.Earning}$ ")
                self.Earning += 500
                print(f"You are good worker and you get: \t500$\n"
                      f"Now your bugget:\t{self.Earning}$ ")
                iphone15price = 1400
                iphone15 = 0
                self.Earning -= iphone15price
                print(f"You bought Iphone 15 Pro Max, it costs you: \t1400$\n"
                      f"Now your bugget:\t{self.Earning}$")
                print("----------------------------------------------")










