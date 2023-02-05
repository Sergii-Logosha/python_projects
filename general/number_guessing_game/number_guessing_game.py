# 05.02.23 Sergii Logosha sergiilogosha@gmail.com

# User has to guess a number from 1 to 100 that computer has picked
# There are two levels of difficulty: "easy" - user has 10 attempts, "hard" -
# user has 5 attempts

from art import logo
from os import system
from random import randint


def choosing_difficulty_level():
    """
    Returns number of attempts the user has
    """
    level = ''
    while level not in ('easy', 'hard'):
        level = input(
            'Choose difficulty level of the game, "easy" or "hard": ')
        if level != 'easy' and level != 'hard':
            print("Plese type in proper level")
    if level == 'easy':
        attempts_number = 10
    elif level == 'hard':
        attempts_number = 5

    return attempts_number


play_again = True
while play_again:
    system('clear')
    selected_number = randint(1, 100)

    print(logo)
    print('Welcome to Number Guessing Game!\nI have picked a number from 1 to '
          '100, guess it.')
    attempts_number = choosing_difficulty_level()
    game_off = False
    while not game_off:
        for i in range(attempts_number):
            print(f'You have {attempts_number} attempts to guess the number')
            print('Please pick a number from 1 to 100')
            guess = 0
            while guess not in range(1, 101):
                guess = int(input('Make your guess: '))
            if guess == selected_number:
                print(f'You got it! Guessed number was {selected_number}')
                game_off = True
                break
            elif guess < selected_number:
                print('Too low')
            elif guess > selected_number:
                print('Too high')
            attempts_number -= 1
            if attempts_number == 0:
                print('You have used all guesses. You loose!')
                game_off = True

    if input('Would you like to play game again(y/n): ') == 'y':
        play_again = True
    else:
        play_again = False
