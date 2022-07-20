# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

import math
seq_1 = []
start_number = 1
number = int(input("Введите число N: "))
for i in range(start_number,number+1):
    seq_1.append(i)
seq_2 = seq_1[:]

for i in range(len(seq_2)):
    seq_2[i] = math.factorial(seq_2[i])
  
print('Пусть N =',number,'тогда',seq_1,seq_2)