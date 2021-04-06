#!/usr/bin/env python
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello, Erol!")
    print("How are you, doing?")
    print("The weather is nice!")
greet()
print("--------------------------")

def greet_a(name):
    print(f"Hello, {name}!")
    print(f"How are you doing, {name}?")
    print("The weather is nice!")
greet_a("Erol")
greet_a("Angela")
print("--------------------------")

def greet_with_a(sender, receiver):
    print(f"Hello, {receiver}!")
    print(f"I am {sender}")
    print("How are you doing?")
greet_with_a("Erol", "Angela")
print("--------------------------")

def greet_with(sender, receiver):
    print(f"Hello, {receiver}!")
    print(f"I am {sender}")
    print("How are you doing?")
greet_with(sender="Erol", receiver="Angela")
print("--------------------------")
