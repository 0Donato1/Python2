'''
students = {1: 'Dima', 2: 'Roma', 3: 'Igor'}

print(students)

iterator = iter(students)
for student in iterator:
    print(student)
'''

#2 Iterator
'''
from Counter import Counter


counter = Counter(9, 0)
for i in counter:
    print(i)
'''

#3 Generator

from generator import Generator

generator = Generator(0)
p = 0
for i in generator.Rise_to_the_degrees_F(3, 10):
    print(f"{p} - {i}")
    p += 1

