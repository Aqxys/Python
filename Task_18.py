# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import random

list1 = []
for i in range(0,10):
    list1.append(int(random()*10))

list2 = []

for i in list1:
    count = 0
    for j in list1:
        if i == j:
            count +=1
    if count == 1:
        list2.append(i)

print(f'в последовательности {list1} не повторяются числа {list2}')