import logging

class Calculator:
    def __init__(self, digit1:int, digit2:int, operation:str, result):
        self.Digit1 = digit1
        self.Digit2 = digit2
        self.Operation = operation
        self.Result = result
        logging.basicConfig(filename="CalculateErrors.log", filemode='a', level=logging.ERROR)

    def Calculate(self):
        try:
            if (self.Operation.lower() == '+'):
                if (self.Digit1 + self.Digit2 == self.Result):
                    print(f"Right answer {self.Digit1} + {self.Digit2} = {self.Result}")
                assert self.Digit1 + self.Digit2 == self.Result, f"{self.Digit1} {self.Operation} {self.Digit2} != {self.Result} - Wrong answer"

            elif (self.Operation.lower() == '-'):
                if (self.Digit1 - self.Digit2 == self.Result):
                    print(f"Right answer {self.Digit1} - {self.Digit2} = {self.Result}")
                assert self.Digit1 - self.Digit2 == self.Result, f"{self.Digit1} {self.Operation} {self.Digit2} != {self.Result} - Wrong answer"

            elif (self.Operation.lower() == '//'):
                if (self.Digit1 / self.Digit2 == self.Result):
                    print(f"Right answer {self.Digit1} / {self.Digit2} = {self.Result}")
                assert self.Digit1 / self.Digit2 == self.Result, f"{self.Digit1} {self.Operation} {self.Digit2} != {self.Result} - Wrong answer"

            elif (self.Operation.lower() == '*'):
                if (self.Digit1 * self.Digit2 == self.Result):
                    print(f"Right answer {self.Digit1} * {self.Digit2} = {self.Result}")
                assert self.Digit1 * self.Digit2 == self.Result, f"{self.Digit1} {self.Operation} {self.Digit2} != {self.Result} - Wrong answer"

        except AssertionError as ae:
            logging.error(ae)
