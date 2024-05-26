# Hangman Project - Milestone_2 File
import random 

# Task 1: Create a list of 5 favorite fruits
fruit_list = [
             "kiwi", "banana", "apple", 
             "watermelon", "tomato",
             ]
word_list = fruit_list

print(word_list)

# Task 2: Choose a random word from the list
word = random.choice(word_list)

print(word)

# Task 3: Ask user for input
guess = input("Input 1 letter: ")

# Task 4: Check that input is a single character
if (len(guess) == 1 and 
    guess.isalpha() == True):
    # Checks user input is both a letter and 1 character long    
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
