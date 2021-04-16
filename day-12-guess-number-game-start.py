#!/usr/bin/env python
import random
from diverse_logos import number_guessing_logo

print(number_guessing_logo)
print("Welcome to the Number Guessing Game!")

def difficulty():
    """
    Ask user to choose between difficulty level 'easy' and 'hard'
    """
    userChoice = ''
    try:
        userChoice = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if userChoice == 'hard':
            attempts = 5
            return attempts
        else:
            attempts = 10
            return attempts
    except:
        print(f"You have typed '{userChoice}'. Type 'easy' or 'hard': ")

def guessNumber(attempts):
    """
    Make user guess the number the computer randomly generated
    """
    while attempts > -1:
        print(f"You have {attempts} attempts remaining to guess the number")
        userGuess = input("Make a guess: ")
        try:
            userGuess = int(userGuess)
            if userGuess > computerNum:
                print("Too high.")
                attempts -= 1
                if attempts == 0:
                    print(f"You lose! 😱 I was thinking of {computerNum}.")
                    break
                else:
                    print("Guess again!")
            elif userGuess < computerNum:
                print("Too Low.")
                attempts -= 1
                if attempts == 0:
                    print(f"You lose! 😱 I was thinking of {computerNum}.")
                    break
                else:
                    print("Guess again!")
            else:
                print("You guessed right. You won 😃")
                break
        except ValueError:
            if not userGuess:
                print('You have not entered anything! Type a number.')
            else:
                print(f"You've typed '{userGuess}'. Type a number instead")

exit_game = False

while not exit_game:
    computerNum = random.randint(1,100)
    print("I'm thinking of a number between 1 and 100")
    print(f"Pssst, the correct answer is {computerNum}") # for dev purposes
    attempts = difficulty()
    guessNumber(attempts)
    try:
        anotherRound = input("Would you like to play again? 'y' or 'n': ")
        if anotherRound == 'n':
            exit_game = True
    except:
        print(f"'y' or 'no'")
