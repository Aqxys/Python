# Создайте программу для игры с конфетами человек против человека.

from random import randint
import os
os.system('cls' if os.name == 'nt' else 'clear')

def player_turn(number, name):
    while True:
        number = int(input('\n Игрок '+ str(name) +', введите число конфет от 1 до 28: '))
        if 1 <= number <= 28:
            break
        else:
            print('Введите число от 1 до 28')     
    return number

def computer_turn(number):
    number = randint(1,28)
    print(f'\n Компьютер берет {number} конфет')
    return number

def game_start(lottery):
    if lottery == 0:
        print(f'Игру начинает Игрок 1. В игре {game_count} конфет')
    elif lottery == 1:
        print(f'Игру начинает Игрок 2. В игре {game_count} конфет')

def game_start_comp(lottery):
    if lottery == 0:
        print(f'Игру начинает Игрок 1. В игре {game_count} конфет')
    elif lottery == 1:
        print(f'Игру начинает компьютер. В игре {game_count} конфет')

def game_over(n):
    if n == 0:
        print('\n Игра закончена. Победитель Игрок 1')
    elif n == 1:
        print('\n Игра закончена. Победитель Игрок 2')

def game_over_comp(n):
    if n == 0:
        print('\n Игра закончена. Победитель Игрок 1')
    elif n == 1:
        print('\n Игра закончена. Победитель компьютер')
   
game_count = 100
player_1 = 0
player_2 = 0
a = int(input('Игра в ' + str(game_count) +' конфет: \n Игрок против игрока - 1 \n Игрок против компьютера - 2 \n введите число: '))

if a == 1:
    lottery = randint(0,1)
    game_start(lottery)
    while game_count >= 1:
        while lottery == 0: 
            player_1 = int(player_turn(player_1, 1))
            game_count -= player_1
            lottery += 1
            print(f'В игре {game_count} конфет')
            if game_count <= 0:
                break        
        else:
            lottery == 1
            player_2 = int(player_turn(player_2, 2))
            game_count -= player_2
            lottery -= 1
            print(f'В игре {game_count} конфет')
    if game_count <=0:
        game_over(lottery)
else:
    lottery = randint(0,1)
    game_start_comp(lottery)
    while game_count >= 1:
        while lottery == 0: 
            player_1 = int(player_turn(player_1, 1))
            game_count -= player_1
            lottery += 1
            print(f'В игре {game_count} конфет')
            if game_count <= 0:
                break        
        else:
            lottery == 1
            player_2 = int(computer_turn(player_2))
            game_count -= player_2
            lottery -= 1
            print(f'В игре {game_count} конфет')
    if game_count <=0:
        game_over_comp(lottery)