#!/usr/bin/env python
from random import randint
from diverse_logos import number_guessing_logo

# Global constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard'. ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# function to check user's guess against random number (answer)
# track number of turns and reduce by 1, if user's guess is wrong
def check_answer(guess, answer, turns):
    """
    checks answer against guess. Returns the number of turns remaining.
    """
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def game():
    """
    The logic of number guessing game
    """
    print(number_guessing_logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    turns = set_difficulty()
# produce a random number (answer) between 1 and 100
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    guess = 0
    # repeat function to check user's guess, if user's guess is wrong
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        # let user guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return # a simple return, exits the function
        elif guess != answer:
            print("Guess again.")

game()

