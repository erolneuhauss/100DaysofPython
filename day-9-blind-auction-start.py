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

auction_dict = {
    "Sissi": 10,
    "Erol": 20,
    "Mel": 50,
    "Zebra": 30,
    "Alfred": 100
    }
#print(auction_list)
print(auction_dict)

highest_value = max(auction_dict.values())
print(highest_value)

highest_bidder = max(auction_dict, key=auction_dict.get)
print(highest_bidder)

print(f"Highest bidder is {highest_bidder} who has bid {auction_dict[highest_bidder]}")

def add_auctioners(bidder_name, bidder_value):
    auction_dict[bidder_name] = bidder_value

should_continue = True
while should_continue:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    add_auctioners(bidder_name=name, bidder_value=bid)
    should_continue = input("Are there other users who want to bid?"+
                            "Type 'yes'. Otherwise type 'no'\n")
    if should_continue == "no":
        print("Goodbye!")
        should_continue = False
    else:
        clear()
print(auction_dict)

highest_bidder = max(auction_dict, key=auction_dict.get)
print(highest_bidder)
print(f"Highest bidder is {highest_bidder} who has bid {auction_dict[highest_bidder]}")

