#!/usr/bin/env python
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
user_score = 0
computer_score = 0
# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def deal_card():
    user_cards = random.sample(cards, k=2)
    computer_cards = random.sample(cards, k=2)
    print(user_cards)
    print(computer_cards)
    return (user_cards, computer_cards)

def calculate_score(user_cards, computer_cards):
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    print(user_score)
    print(computer_score)
    if user_score == 21:
        print("User has blackjack")
    if computer_score == 21:
        print("Computer has blackjack")

user_cards, computer_cards = deal_card()
calculate_score(user_cards, computer_cards)
