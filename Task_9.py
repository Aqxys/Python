# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции вводит пользователь через пробел. 

sum = 1
n = int(input('Введите число: '))
array = list(range(-n,n+1))

while True:
    try:
        positions = input("Введите позиции через пробел: ")
        positions = positions.split(" ")
        break
    except ValueError:
        print("Введите целые числа через пробел")

for index in positions:
    sum *= array[int(index)]
print('Произведение элементов в заданном списке:',sum)