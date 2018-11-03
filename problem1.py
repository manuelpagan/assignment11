# Manny Pagan
# Sept 24th Python Course
# Assignment 11
# Due Nov 5th



import random

guess = 0
answer = random.randint(1, 100)
print("Let's try a guessing game, pick a number between 1 and 100:")
guess = int(input())

if 0 <= guess <= 100:
    while guess != answer:
        if guess > answer:
            print('That is too high! Guess again...', end='')
        else:
            print('That is too low! Guess again...', end='')
        guess = int(input())

        if guess == answer:
            print("That's it! You win! The number was", answer)
else:
    print("Choose a number between 1 and 100 and try again.")
