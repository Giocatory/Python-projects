# Игра - угадай число
import random


def writeYourNumber():
    """Проверка ввода числа игрока"""
    guess = ''
    while True:
        guess = input('Угадай число: ')
        try:
            guess = int(guess)
            if guess < 0 or guess > 100:
                print('Извините, но у нас диапазон от 0 до 100!')
                continue
            break           
        except:
            print('Введено не число, попробуй снова!')
            continue
    return guess


myName = input('Привет, как тебя зовут?\n~')
number = random.randint(1, 100)
countChoices = 0
print(f'Что ж, {myName} я загадываю число от 0 до 100!')

while True:
    choice = writeYourNumber()
    countChoices += 1
    if choice > number:
        print('Попробуй число поменьше!')
        continue
    if choice < number:
        print('Попробуй число по больше!')
        continue
    if choice == number:
        print('УУУРРАААА победа!!!!')
        break

print(f'Общее колиство попыток = {countChoices}')
input()