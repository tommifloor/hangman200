# # Hangman Project - Milestone_5 File
import random

# Task 1: Create Hangman Class

# Class constructor
class Hangman:
    def __init__(self, word_list, num_lives=5):
        
        # Attributes
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed =  ["_" for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

# Task 2: Create methods

    # Methods
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! \"{guess}\" is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                   self.word_guessed[i] = guess
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Sorry, \"{guess}\" is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if  (len(guess) != 1 or 
                guess.isalpha() == False):
                # Check user input is 1 character long and alphabetical
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

play_game(["apple","banana","peach"])