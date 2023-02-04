'''
Write a Python program that takes in an integer that a player will attempt to guess. The program should display
"too high" if the guess is higher and "too low" if the guess is lower. The program will not stop unless the player
guesses the correct integer and print out the number of guesses the player took. The program should executed as follow:

Enter the number for the player to guess.
-10 Enter your guess.
10 Too high - try again:
5 Too high - try again:
-200 Too low - try again:
-10 You guessed it in 4 tries.
'''


import random

secret_number = random.randint(0, 100)
print(secret_number)
guessed_number = int(input('Enter the number for the player to guess:'))
number_of_guesses = 0


def guessing(guessed_number, number_of_guesses):
    if guessed_number < secret_number:
        number_of_guesses += 1
        print(f'The guessed number {guessed_number} is too low, try again:')
        guessed_number = int(input())
        guessing(guessed_number, number_of_guesses)
    elif guessed_number > secret_number:
        number_of_guesses += 1
        print(f'The guessed number {guessed_number} is too high, try again:')
        guessed_number = int(input())
        guessing(guessed_number, number_of_guesses)
    elif guessed_number == secret_number:
        number_of_guesses += 1
        if number_of_guesses == 1:
            print('Well done! You guessed it in first try.')
        else:
            print(f'Nice, you guessed {guessed_number} and it was correct!.')
            print(f'You found the number in {number_of_guesses} tries.')


guessing(guessed_number, number_of_guesses)