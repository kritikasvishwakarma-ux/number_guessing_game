# a number guessing game where the user has to guess a random number between 1 and 10.  The user has a limited number of guesses, and the game provides feedback on whether the guess is correct or not. 
# If the user runs out of guesses, they lose the game.

import random

print('welcome to the number guessing game!')
print('\nyou have 3 chances to guess the number between 1 and 10')
print('the secret number is between 1 and 10')

#difficulty level
print('\n choose a difficulty level: easy, medium, hard')
print('\n easy: 5 chances' )
print(' medium: 3 chances')
print(' hard: 1 chance')

difficulty = input("\n enter difficulty level:")
if difficulty == 'easy':
    guess_limit = 5
elif difficulty == 'medium':
    guess_limit = 3
elif difficulty == 'hard':
    guess_limit =1
else:
    print(' invalid difficulty level, defaulting to medium.')
    guess_limit = 3

secret_number = random.randint(1, 10)
guesses = 0
while guesses < guess_limit:
    guess = int(input('\n enter your guess between 1 and 10:'))
    guesses += 1

    #check if the guess is correct
    if guess == secret_number:
        score = guess_limit - guesses + 1
        print('\n congratulations! you guessed the number in', guesses, 'guesses!')
        print(' your score is:', score)
        break

    #helpful feedback for the user to know if their guess is too high or too low
    elif guess < secret_number:
        print('\n too low, try again!')
    elif guess > secret_number:
        print('\n too high, try again!')

#if the user runs out of guesses, they lose the game
else:
    print('\n you are out of guesses, you lose! The number was', secret_number)
print('\n thanks for playing!')
print(' start a new game by running the program again!')