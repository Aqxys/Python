# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов

import pathlib

path_1 = pathlib.Path.cwd()/'Programming_lessons'/'Python'/'Solution_20.txt'
path_2 = pathlib.Path.cwd()/'Programming_lessons'/'Python'/'Solution_21.txt'
with open (path_1, 'r') as file:
    data_1 = file.read()
    file.close()
with open (path_2, 'r') as file:
    data_2 = file.read()
    file.close()

# идем самым топорным методом, когда размеры многочленов заранее известны (обработка данных по шаблону)
# ______________________________________________________
# new_second = int(data_1[7:10]) + int(data_2[0:2])
# new_third = int(data_1[13:16]) + int(data_2[5:7])
# data_3 = data_1[0:2] + data_1[2:5] + ' + ' + str(new_second) + 'x' + ' + ' + str(new_third) + ' = 0'
# print(f'Сумма многочленов {data_1} и {data_2} -> {data_3}')

# фигура вторая, универсальная
# ______________________________________________________
new_data_1 = data_1.split()
new_data_2 = data_2.split()
part_1 = ''
part_2 = ''
part_3 = ''

# уравнения полные и равны
if (len(new_data_1)) > 6 and (len(new_data_1)) == (len(new_data_2)):
    part_1 = int((new_data_1[0])[0:2]) + int((new_data_2[0])[0:2])
    part_2 = int((new_data_1[2]).strip('x')) + int((new_data_2[2]).strip('x'))
    part_3 = int(new_data_1[4]) + int(new_data_2[4])
    data_3 = str(part_1) + (new_data_1[0])[2:5] + ' + ' + str(part_2) + 'x + ' + str(part_3) + ' = 0'

# уравнения средние и равны
elif (len(new_data_1)) > 4 and (len(new_data_1)) == (len(new_data_2)):
    part_2 = int((new_data_1[0]).strip('x')) + int((new_data_2[0]).strip('x'))
    part_3 = int(new_data_1[2]) + int(new_data_2[2])
    data_3 = str(part_2) + 'x + ' + str(part_3) + ' = 0' 

# уравнения короткие и равны
elif (len(new_data_1)) > 2 and (len(new_data_1)) == (len(new_data_2)):
    part_3 = int(new_data_1[0]) + int(new_data_2[0])
    data_3 = str(part_2) + 'x + ' + str(part_3) + ' = 0' 

# первое полное, второе среднее
elif (len(new_data_1)) > 6 and (len(new_data_1)) > 4:
    part_2 = int((new_data_1[2]).strip('x')) + int((new_data_2[0]).strip('x'))
    part_3 = int(new_data_1[4]) + int(new_data_2[2])
    data_3 = new_data_1[0] + ' + ' + str(part_2) + 'x + ' + str(part_3) + ' = 0'

# первое полное, второе короткое
elif (len(new_data_1)) > 6 and (len(new_data_1)) > 2:
    part_3 = int(new_data_1[4]) + int(new_data_2[2])
    data_3 = new_data_1[0] + ' + ' + new_data_1[2] + str(part_3) + ' = 0'

# первое среднее, второе полное
elif (len(new_data_1)) > 4 and (len(new_data_1)) > 6:
    part_2 = int((new_data_1[2]).strip('x')) + int((new_data_2[0]).strip('x'))
    part_3 = int(new_data_1[4]) + int(new_data_2[2])
    data_3 = new_data_2[0] + ' + ' + str(part_2) + 'x + ' + str(part_3) + ' = 0'

# первое короткое, второе полное
elif (len(new_data_1)) > 2 and (len(new_data_1)) > 6:
    part_3 = int(new_data_1[4]) + int(new_data_2[2])
    data_3 = new_data_2[0] + ' + ' + new_data_2[2] + str(part_3) + ' = 0'

# первое среднее, второе короткое
elif (len(new_data_1)) > 6 and (len(new_data_1)) > 2:
    part_3 = int(new_data_1[4]) + int(new_data_2[2])
    data_3 = new_data_1[0] + str(part_3) + ' = 0'

# первое короткое, второе среднее
elif (len(new_data_1)) > 6 and (len(new_data_1)) > 2:
    part_3 = int(new_data_1[4]) + int(new_data_2[2])
    data_3 = new_data_2[0] + str(part_3) + ' = 0'


print(data_3)

# записываем результат в файл
path_3 = pathlib.Path.cwd()/'Programming_lessons'/'Python'/'Solution_20_21.txt'
with open (path_3, 'w') as file:
    file.write(data_3)
    file.close()