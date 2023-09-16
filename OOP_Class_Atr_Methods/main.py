from student import Student

budnychenko = Student("Denys", 15.7, "S2816", 1600.00)
solop = Student("Illya", 16.1, "S2816", 105.00)
oliynyk = Student("Kostya", 14.2, "S2816", 165.00)

students = []

students.append(budnychenko)
students.append(solop)
students.append(oliynyk)

for student in students:
    student.ShowInfo()
print("----------------------------------------------------------------------")
iphone15price = 1400
budnychenko.Buy(iphone15price)
solop.Buy(iphone15price)
oliynyk.Buy(iphone15price)

for student in students:
    student.ShowInfo()
'''
days = 365
for day in days:
    if(day > 358 and day < 7):
'''





