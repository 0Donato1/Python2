from HW6 import Calculator

a = int(input("Enter digit: "))
b = int(input("Enter digit: "))
operation = input("Enter operation: ")
result = int(input("Enter result: "))
tester = Calculator(a, b, operation, result)
tester.Calculate()
