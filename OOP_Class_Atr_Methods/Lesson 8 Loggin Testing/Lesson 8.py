import logging

#1 logging
'''
logging.basicConfig(filename="logs.log", filemode='a', level=logging.DEBUG)#filemode='w' - write, filemode='a' - append

logging.debug("Debug")
logging.info("Info")
logging.warning("Warning")
logging.error("Error")
logging.critical("Critical")
'''

#2 logging
'''
import logging

logger = CustomLog('logs.log', logging.CRITICAL)

try:
    result = 10/0
except ZeroDivisionError as zde:
    logger.SetUpConfig()
    logging.critical(zde)
'''

#3 testing
'''
if 2 + 2 == 4:
    print("True")
else:
    print("False")
'''

'''
from LogExample import CustomLog
logger = CustomLog('logs.log', logging.ERROR)
logger.SetUpConfig()
        

try:
    a = int(input("Enter digit: "))
    b = int(input("Enter digit: "))
    operation = input("Enter operation: ")
    result = int(input("Enter result: "))

    if(operation.lower() == '+'):
        assert a + b == result, f"{a} + {b} != {result} - Wrong answer"
    elif (operation.lower() == '-'):
        assert a - b == result, f"{a} - {b} != {result} - Wrong answer"
    elif (operation.lower() == '*'):
        assert a * b == result, f"{a} * {b} != {result} - Wrong answer"
    elif (operation.lower() == '//'):
        assert a / b == result, f"{a} / {b} != {result} - Wrong answer"

except AssertionError as ae:
    logging.error(ae)
'''

#4

from TestExample import Tester

a = int(input("Enter digit: "))
b = int(input("Enter digit: "))
operation = input("Enter operation: ")
result = int(input("Enter result: "))
tester = Tester(a, b, operation, result)
tester.CheckCalculate()



#5
'''
"""
>>>assertion
result
"""
'''

"""
>>>5+2
8
"""
'''
if __name__ == "__Lesson8__":
    import doctest
    doctest.testmod()
'''

