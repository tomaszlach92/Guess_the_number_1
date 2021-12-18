"""Guess the number game"""
from random import randint

GUESS = False
NUMBER = randint(1, 100)

while not GUESS:
    try:
        user_number = float(input("Guess the number:"))
        if NUMBER == user_number:
            GUESS = True
            print("You win!")
        elif NUMBER < user_number:
            print("To big!")
        elif NUMBER > user_number:
            print("To small!")
    except ValueError:
        print("It's not a number!")
