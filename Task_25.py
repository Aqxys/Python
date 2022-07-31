# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import random

# задаем список случайных чисел с помощью генератора и одноразовой анонимной функции
f = lambda x: int(random()*10)
list1 =[f(i) for i in range(1,11)]

# ищем неповторяющиеся элементы с помощью функции count
list2 =[i for i in list1 if list1.count(i) == 1]
print(f'в последовательности {list1} не повторяются числа {list2}')

# используем filter для поиска четных чисел 
even_numbers = list(filter(lambda x: x%2 == 0, list2))
print(f'из них четные числа: {even_numbers}')

# и map для проведения некоей операции над этими найденными числами
demo_result = list(map(lambda x: x**3, even_numbers))
print(f'кубы этих чисел: {demo_result}')