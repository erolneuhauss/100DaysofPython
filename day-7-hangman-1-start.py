#!/usr/bin/env python3
# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and
# assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter
# and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
print("Your have guessed:", guess)

# TODO-3 - Check if the letter the user guessed (guess)
# is one of the letters in the chosen_word
if guess in chosen_word:
    print(guess, " is in the word")
else:
    print("You have guessed wrong")

# Finding all indexes of a string in the list
# with while loop
print("----- while loop -----")
matched_indexes = []
index = 0
length = len(chosen_word)
while index < length:
    if guess == chosen_word[index]:
        print("Right")
        matched_indexes.append(index)
    else:
        print("Wrong")
    index += 1

print("----- for loop if equal --")
# with for loop
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

print("----- for loop if in -----")
# with for loop
for letter in chosen_word:
    if letter in guess:
        print("Right")
    else:
        print("Wrong")
