# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# k=2 => 2*x² + 4*x + 5 = 0

import random
import pathlib

k = int(input('Введите коэффициент: '))
a = int(random.randint(0,100))
b = int(random.randint(0,100))
c = int(random.randint(0,100))

if a != 0:
    first_part = (str(a) + "x^" + str(k) + " + ")
else:
    first_part = (str())

if b != 0:
    second_part = (str(b) + "x" + " + ")
else:
    second_part = (str())

if c != 0:
    third_part = (str(c) + " = 0")
else:
    third_part = (str())

print(f'{first_part}{second_part}{third_part}')

path = pathlib.Path.cwd()/'Programming_lessons'/'Python'/'Solution_19.txt'
with open (path, 'w') as file:
    file.write(f'{first_part}{second_part}{third_part}')
    file.close()