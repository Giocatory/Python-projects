from hangmanScheme import HANGMAN_PICS_SCHEME
import random

def getRandomWord(wordList):
    '''Random word in argument list'''
    wordIndex = random.randint(0, len(wordList)-1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS_SCHEME[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # Заменяет пропуски отгаданными словами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    
    for letter in blanks:  # Показывает секретное слово с пробелами между букв
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    '''Возвращает букву, введеную игроком. Эта функция проверяет, что игрок ввел только одну букву и ничего больше'''
    while True:
        guess = input('Введите букву: ').lower()
        if len(guess) != 1:
            print('Пожалуйста введите одну букву')
        elif guess in alreadyGuessed:
            print('Вы уже вводили эту букву. Введите другую!')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъьэюяы':
            print('Неправильный символ или число, введите букву русского алфавита!')
        else:
            return guess


def playAgain():
    '''Возвращает TRUE, если игрок хочет играть сначала,
    в противном случае возвращает FALSE'''
    print('Хотите сыграть еще? (введите да или нет)')
    return input().lower().startswith('д')
