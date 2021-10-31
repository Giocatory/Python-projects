# Игра - угадай число
import random


def writeYourNumber():
    guess = ''
    while True:
        guess = input('Угадай число: ')
        try:
            guess = int(guess)
            break           
        except:
            print('Введено не число, попробуй снова!')
            continue
    return guess


myName = input('Привет, как тебя зовут?\n~')
number = random.randint(1, 100)
countChoices = 0
print(f'Что ж, {myName} я загадываю число от 1 до 100!')

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
