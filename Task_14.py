# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input('Введите число: '))
dec = ''
while number > 0:
    dec += str(number % 2)
    number = number // 2
print(dec)