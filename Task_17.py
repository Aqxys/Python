# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите число: '))

def simple_dividers (n):
    list_of_dividers = list()
    div = 2
    while div <= n:
        if n % div == 0:
            list_of_dividers.append(div)
            n = n/div
        else:
            div +=1
    return list_of_dividers

print(f'Простые делители числа {number}: {simple_dividers(number)}')