# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

import pathlib

def encoding(data):
    prev_char = ''
    new_data = ''
    count = 1
    for i in data:
        if i != prev_char:
            if prev_char:
                new_data += str(count) + prev_char
            count = 1
            prev_char = i
        else:
            count += 1
    else:
        new_data += str(count) + prev_char

    return new_data

def decoding(data):
    new_data = ''
    count = ''
    for i in data:
        if i.isdigit():
            count += i
        else:
            new_data += i * int(count)
            count = ''
    return new_data

path_1 = pathlib.Path.cwd()/'Programming_lessons'/'Python'/'Solution_24_1.txt'
with open (path_1, 'r') as file:
    text_1 = file.read()
    file.close()

text_2 = (str(encoding(text_1)))
text_3 = (str(decoding(text_2)))

path_2 = pathlib.Path.cwd()/'Programming_lessons'/'Python'/'Solution_24_2.txt'
with open (path_2, 'w') as file:
    file.write('Encoding text:' + text_2 + '\nDecoding text:' + text_3)
    file.close()