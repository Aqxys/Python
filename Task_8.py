# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

n = int(input('Введите число: '))
result = 0
count = 0
summ = 0
for i in range(1, n +1 ):
    result = (1 + 1/i)**i
    count += 1
    print(count,':',round(result), end="" '  ')
    summ += result
print()
print('сумма чисел:', round(summ))