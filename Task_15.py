# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

k = int(input('Введите число: '))

def get_fibonacci(n): 
    fib_numbers = []
    a, b = 1, 1
    for i in range(n):
        fib_numbers.append(a)
        a, b = b, a + b
    return fib_numbers
    
fib_norm = get_fibonacci(k)
fib_neg = list(reversed(fib_norm)) 
for i in range(len(fib_neg)):  
    if k % 2 ==0:
        if i % 2 == 0: 
            fib_neg[i] *= -1
    else:
        if i % 2 != 0: 
            fib_neg[i] *= -1
fib_neg.append(0)              
print(f'для k = {k} список будет выглядеть так:', fib_neg + fib_norm)