result = []
def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b
try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
except TypeError as te:
    print("Wrong amount was entered!")
try:
    for key in data:
        res = divider(key, data[kem])
        result.append(res)
except NameError as ne:
    print("Wrong amount was entered!")


print(result)

