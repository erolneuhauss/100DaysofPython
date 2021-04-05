#!/usr/bin/env python

from diverse_logos import gavel_logo
from os import system, name
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

print(gavel_logo)

auction_dict = {
    "Buffy": 12,
}

def find_highest_bidder(auction_dict):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in auction_dict:
        bid_amount = auction_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

should_continue = True
while should_continue:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    auction_dict[name] = bid
    should_continue = input("Are there other users who want to bid?"+
                            "Type 'yes'. Otherwise type 'no'\n")
    if should_continue == "no":
        print("Goodbye!")
        should_continue = False
        find_highest_bidder(auction_dict)
    else:
        clear()


