#!/usr/bin/env python

import os
from random import choice
from diverse_logos import higher_lower_logo, higher_lower_vs
from game_data import data

def determine_answer(A, B):
    """
    determine right answer by comparing follower_count between A and B
    """
    if A['follower_count'] > B['follower_count']:
        answer = 'A'
        return answer
    else:
        answer = 'B'
        return answer

print(higher_lower_logo)
score = 0
is_game_over = False
A = choice(data)
while not is_game_over:
    print(f"\nCompare A: {A['name']}, {A['description']}, {A['country']}, {A['follower_count']}.")
    print(higher_lower_vs)
    B = choice(data)
    print(f"Against B: {B['name']}, {B['description']}, {B['country']}, {B['follower_count']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ")
    answer = determine_answer(A, B)

    os.system('cls||clear')
    print(higher_lower_logo)
    if guess == answer:
        score += 1
        print(f"You're right! Current score: {score} ")
        A = B
    else:
        print(f"Sorry, that's wrong. Final score: {score} ")
        is_game_over = True




