import random
import time


def displayIntro():
    print("""Вы находитесь в землях, заселенных драконами. Перед собой вы видите две пещеры.
В одной из них — дружелюбный дракон, который готов поделиться с вами своими сокровищами.
Во второй — жадный и голодный дракон, который мигом вас съест.\n""")


def chooseCave():
    cave = ''
    while True:
        cave = input('В какую пещеру пойдете? (нажмите клавишу 1 или 2)\n~')
        if cave != '1' and cave != '2':
            print('Вы можете выбрать только 1 или 2')
            continue
        else:
            break
    return cave


def checkCave(chosenCave):
    print('Вы приближаетесь к пещере...'); time.sleep(2)
    print('Её темнота заставляет вас дрожать от страха...'); time.sleep(2)
    print('Большой дракон выпрыгивает перед вами! Раскрывает пасть и...'); time.sleep(2)
    print(); time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('... делится с вами сокровищами!!!')
    else:
        print('... Вкусно чавкает вашими остатками!!!\n')

playAgain = 'да'

while playAgain.lower() in ['да', 'д', 'y', 'yes']:
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    playAgain = input('Сыграете еще раз? (введите да или нет)\n~')

print('Спасибо за игру!!!')
input()