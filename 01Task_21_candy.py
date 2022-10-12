# ; Создайте программу для игры с конфетами человек против человека.

# ; Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# ; a) Добавьте игру против бота

# ; b) Подумайте как наделить бота ""интеллектом""

import random
candy = 2021
ostatok = 2021 % 29  # крайнеи случаи  игрок взял 1 конфету бот 28 =29 и наоборот игрок 28 бот 1 Поэтому 29. Остаток деоения на 29 от  2021 это 20. Поэтому ироку при первом ходе надо взять 2 конфет, а дальше доводить 29 в зависисмости от хода бота.
print(ostatok)
print('Кинем жребий, кто первый ходит 1-бот, 2-игрок')
zhreby = random.randint(1, 2)
print(zhreby)
if zhreby == 1:
    #khod = 1
    print('Первый ходит бот')
    khod_bota = random.randint(1, 28)
    print('бот взял', khod_bota, ' конфет')
    candy = candy-khod_bota
    khod_player = int(input('Ходи кожанный'))
    candy = candy-khod_player
    print('осталось ', candy, ' конфет')

# else:
#     #khod = 2
#     khod_player = int(input('Ходи кожанный'))
#     candy = candy-khod_player
#     print('осталось ', candy, ' конфет')
if zhreby == 2:
    khod_player = int(input('Ходи кожанный'))
    candy = candy-khod_player
    print('осталось ', candy, ' конфет')


i = 2
while candy > 0:
    # if khod == 1:
    #     khod_bota = random.randint(1, 28)
    #     candy = candy-khod_bota
    #     print('Ход бота №', i, ' ', khod_bota, 'конфет')
    #     print('Осталось ', candy, 'конфет')
    #     khod = 0
    #     i += 1

    khod_bota = random.randint(1, 28)
    candy = candy-khod_bota
    if candy == 0:
        print('Бот выйграл')
        break
    print('Ход бота №', i, ' ', khod_bota, 'конфет')
    print('Осталось ', candy, 'конфет')
    #khod = 0

    khod_player = int(input('Ход игрока'))
    print('Ход тгрока №', i)
    candy = candy-khod_player
    print('осталось ', candy, ' конфет')
    if candy == 0:
        print('Бот выйграл')
        break
    i += 1
