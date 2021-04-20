#!/usr/bin/env python

import os
import random

from diverse_logos import higher_lower_logo, higher_lower_vs
from game_data import data


def format_data(account):
    """
    Format the account data and return into printable format.
    """
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    account_follower_count = account["follower_count"]
    return (
        f"{account_name}, a {account_desc}, from {account_country}"
        f"(Pss! Hint: Follower count: {account_follower_count})"
    )


def check_answer(guess, a_followers, b_followers):
    """
    Take the user guess and followers count and returns if they got it right
    """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display art
print(higher_lower_logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:
    # Generate a random account from the game data.
    # Make account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}.")
    print(higher_lower_vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    # Get follower_count count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    # Use if statement to check if user is correct.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # Clear the screen
    os.system("cls||clear")
    print(higher_lower_logo)

    # Give user feedback on their guess.
    # Score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Your final score: {score}")
