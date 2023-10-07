import requests

import colorama

#ALL FUNCTIONS
'''
attrs = dir(requests)
for i in attrs:
    print("-------------")
    print(i)
'''

#CHECKING ELEMENT
'''
print(hasattr(requests, "__url__"))
print(hasattr(requests, "ConnectionError"))
print(getattr(requests, "ConnectionError"))
'''

attrs = dir(colorama)
for i in attrs:
    print("-------------")
    print(i)