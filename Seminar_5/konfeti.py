# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

print('правила игры:\nНа столе лежит 2021 конфета.\nИграют два игрока делая ход друг после друга.\nПервый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.\n----Жребий брошен!!!---\n')
candy = 2021
jrebiy = random.randint(0, 1)

if jrebiy == 0: print('начинает игру Игрок 1')
if jrebiy == 1: print('игру начинает Компьютер')

while candy > 0:
    if jrebiy == 0:
        while True:
            try:
                one_player = int(input("\nигрок 1, введите число:\n"))
                if 0 < one_player <= 28:
                    candy -= one_player
                    if candy > 0:
                        print(f'осталось {candy} конфет')
                        break
                    if candy <= 0:
                        print('\nконфет больше нет.. вы победили, забрав последнюю конфету!\nСыграйте еще раз! ^_^')
                        break
                else:
                    print('Вы ввели неверное число, попробуйте снова!!!')
            except:
                print('вы ввели не верное значение, попробуйте снова!!!')

    if candy <= 0:
        break
    if jrebiy == 0: jrebiy +=1

    if jrebiy == 1:
        print('\nход компьютера:')
        two_compucter = random.randint(1,28)
        print(two_compucter)
        candy -= two_compucter

    if candy >0:
        print(f'осталост {candy} конфет')
    if candy <= 0:
        print('\nконфет больше нет.. компьютер победил, забрав последнюю конфету!\nВы проиграли, попробуйте снова!')
        break
    
    jrebiy -=1

print('Конец Игры!')