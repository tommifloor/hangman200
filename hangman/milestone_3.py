# Hangman Project - Milestone_3 File
import random

# From Mileston_2 File:

fruit_list = [
             "kiwi", "banana", "apple", 
             "watermelon", "tomato",
             ]
word_list = fruit_list

word = random.choice(word_list)

# Task 1: Check if input is a valid
# Moved to ask_for_input function in Task 3

# Task 2: Check whether the guess is in the word
# Moved to check_guess function in Task 3


# Task 3: Create functions to run checks

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if (len(guess) == 1 and 
            guess.isalpha() == True):
            # Check user input is 1 character long and alphabetical
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            
    check_guess(guess)

# Test

ask_for_input()