# Вычислить число c заданной точностью d

number = 0
while number < 1 or number > 10:
    try:
        number = int(input('До какого числа после запятой требуется вычислить Пи: '))
    except ValueError:
        print ('Такая операция невозможна в рамках программы')
pi = 0.0

# задаем коэффициент точности вычисления
if number < 5:
    index = number*100000
else:
    index = number*10000000

# вычисляем пи с помощью ряда Лейбница
for i in range(1, index, 2):
    pi = 4.0 / i - pi

pi_string = str(abs(pi))
print(pi_string)
print(pi_string[0:number+2])

exit()

# ниже второе решение, формулой Бeлларда
# т.к. первое чрезмерно ресурсоемкое и мне не нравится

import math
from decimal import *

number = int(input('До какого числа после запятой требуется вычислить Пи: '))

def bellard(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k/(1024**k))*( Decimal(256)/(10*k+1) + Decimal(1)/(10*k+9) - Decimal(64)/(10*k+3) - Decimal(32)/(4*k+1) - Decimal(4)/(10*k+5) - Decimal(4)/(10*k+7) - Decimal(1)/(4*k+3))
        k += 1
    pi = pi * 1/(2**6)
    return pi

pi_string = str(bellard(number))
print(pi_string[0:number+2])
