class Student:

    def __init__(self, name:str, age:float, group:str, money:float):
        self.Name = name
        self.Age = age
        self.Group = group
        self.Money = money

    def ShowInfo(self):
        print(f"Name:\t{self.Name}\n"
              f"Age: \t{self.Age}\n"
              f"Group:\t{self.Group}\n"
              f"Money:\t{self.Money}$")

    def Buy(self, price:float):
        if(self.Money >= price):
            self.Money -= price
            print("Nice bought!")
        else:
            print(f"Not enough money!\n"
                  f"Your bugget:\t{self.Money}$")
