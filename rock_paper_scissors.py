import random
import time

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
wins = 0
draws = 0
loses = 0

while True:
    player_move = input('Type [r] for Rock, [p] for paper or [s] for scissors: ')

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        player_move = input('Invalid Input. Try again: ')

    computer_random_number = random.randint(1, 3)
    computer_move = ''

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors
    print(f'The computer chose {computer_move}')
    result = ''

    if (player_move == rock and computer_move == scissors)\
            or (player_move == paper and computer_move == rock)\
            or (player_move == scissors and computer_move == paper):
        result = 'You Win!'
        wins += 1
        time.sleep(0.5)
        print(f'\x1b[34m{result}\x1b[0m')
    elif player_move == computer_move:
        time.sleep(0.5)
        result = 'Draw!'
        draws += 1
        print(f'\x1b[33m{result}\x1b[0m')
    else:
        time.sleep(0.5)
        result = 'You Lose!'
        loses += 1
        print(f'\x1b[31m{result}\x1b[0m')

    time.sleep(0.4)
    print(f'The scores are: \x1b[34mWins\x1b[0m: {wins}, \x1b[33mDraws\x1b[0m: {draws}, \x1b[31mLoses\x1b[0m: {loses}')

    if result == 'You Win!' or result == 'Draw!' or result == 'You Lose!':
        player_move = input('Type [yes] to play again or [no] to exit: ')
        if player_move == 'no':
            raise SystemExit('\x1b[42mThank you for playing :)\x1b[0m')
        elif player_move != 'yes':
            player_move = input('Invalid Input. Try again: ')

