# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


list_1 = [1, 2, 3, 4, 5, 6]
list_2 = []
for i in range((len(list_1)+1)//2):
    list_2.append(list_1[i]*list_1[len(list_1)-1-i])
print(f'в списке - {list_1} суммы пар чисел равны: {list_2}')