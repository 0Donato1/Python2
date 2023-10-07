'''
try:
    a = input("Enter digit: ")
    b = input("Enter digit: ")
    print(a/b)
except TypeError:
    try:
            a = float(a)
            b = float(b)
            print(a/b)

    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde}")
    except Exception as ex:
        print(f"Exception: {ex}")

except ZeroDivisionError as zde:
    print(zde)
'''

import warnings

from builderror import BuildError
from validations import Validator

limit = 10
amount = input("Enter amount: ")
#warnings.warn(f"ValueError {amount}")
warnings.simplefilter("error", f"ValueError {amount}")
try:
    amount = int(amount)
    check = Validator()
    check.Check(amount, limit)
except TypeError as te:
    print("Wrong amount was entered!")
except ValueError as ve:
    print(ve)
except BuildError as be:
    print(be)

