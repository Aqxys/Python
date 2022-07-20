# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

number = input("Введите число: ")
digits = [int (x) for x in str(number) if x.isdigit()]
sumofdigit = sum (digits)
print (number,'->',sumofdigit)