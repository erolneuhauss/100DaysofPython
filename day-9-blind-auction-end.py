#!/usr/bin/env python
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(highest_bid)
    print(winner)
    print(f"Highest bidder is {winner} who has bid ${highest_bid}")

while not bidding_finished:
    name = input("What is your name? ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    should_continue = input("Are there any other bidders?"+
                            "Type 'yes'. Otherwise type 'no'\n")
    if should_continue == "no":
        print("Goodbye!")
        bidding_finished = True
        find_highest_bidder(bids)
