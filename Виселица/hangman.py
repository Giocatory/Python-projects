import random
from hangmanScheme import HANGMAN_PICS_SCHEME
from hangmanLogic import displayBoard, getGuess, getRandomWord, playAgain

HANGMAN_PICS = HANGMAN_PICS_SCHEME

words =  '''аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея 
индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось ля-
гушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон 
попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'''.split()

print('Игра - ВИСЕЛИЦА')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    #  Позволяет игроку ввести букву
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Проверяет выйграл ли игрок
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(f'ДА! Секретное слово - "{secretWord}"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Проверка, превысил ли игрок лимит ппыток и програл
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print(f'''Вы исчерпали все попытки!
            Не угадано букв: {str(len(missedLetters))}
            Угадано букв: {str(len(correctLetters))}
            Было загадано слово - {secretWord}''')
            gameIsDone = True
    
    # Хочет ли игрок играть еще
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
input()