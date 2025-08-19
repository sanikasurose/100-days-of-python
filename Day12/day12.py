"""
Name: Day 12 - The Number Guessing Project
Date: August 19, 2025
Author: Sanika Surose
"""

from random import randint
from art import logo

# Constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Functions
def check_answer(guess, answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")

def set_difficulty():
    """Function to set difficulty."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    """Function for the actual game logic."""
    print(logo)
    # Choosing the number
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    # Repeat guessing if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

# Game play
game()


