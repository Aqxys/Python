# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
#  между максимальным и минимальным значением дробной части элементов.


def find_different(any_numbers):
    numbers = [round(x - int(x), 2) for x in(any_numbers)]
    numbers = [x for x in numbers if type(x) == float]
    return max(numbers) - min(numbers)


list = [7.1, 5.2, 3.1, 5, 3.03, 10.01, 9.95]
print(list, '= >', find_different(list))