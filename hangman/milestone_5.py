# Hangman Project - Milestone_5 File
import random

# Class constructor
class Hangman:
    """
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_guessed_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guessed_letter(guess)
        Checks if the letter is in the word.
    ask_for_letter()
        Asks the user for a letter.
    """
    def __init__(self, word_list, num_lives=5):
       
        # Attributes
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed =  ["_" for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guessed_letters = []

    # Methods
    def check_guessed_letter(self, letter_guess):
        """
        Checks if the letter is in the word.
        If it is, it replaces the "_" in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked
        """
        letter_guess = letter_guess.lower()
        if letter_guess in self.word:
            print(f"Good guess! \"{letter_guess}\" is in the word.")
            for letter in range(len(self.word)):
                if self.word[letter] == letter_guess:
                   self.word_guessed[letter] = letter_guess
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Sorry, \"{letter_guess}\" is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_letter(self):
        """
        Asks the user for a letter and checks 4 things:
        1. If the character is a single character
        2. If the character is alphabetical
        3. If the letter has already been tried
        If the letter passes all checks, it calls the check_guessed_letter method.
        If the letter passes all checks, it appends the letter to the list_of_guessed_letters list.
        """
        while True:
            letter_guess = input("Guess a letter: ")
            if  (len(letter_guess) != 1 
                or letter_guess.isalpha() == False):
                # Check user input is 1 character long and alphabetical
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif (letter_guess in self.list_of_guessed_letters
                  or letter_guess.lower() in self.list_of_guessed_letters):
                print("You already tried that letter!")
            else:
                self.check_guessed_letter(letter_guess)
                self.list_of_guessed_letters.append(letter_guess)
                self.list_of_guessed_letters.append(letter_guess.lower())
                break

# Class instance
def play_game(word_list):
    """
    Creates an instance of the Hangman class named game.
    If num_lives is reduced to Zero user loses game.
    If num_letters remain, loops game instance.
    If num_live is greater than zero and user has no num_letters remain, the user wins the game.
    """
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        if game.num_letters > 0:
            game.ask_for_letter()
        else:
            print("Congratulations. You won the game!")
            break

# Run instance
if __name__ == "__main__":
    word_list = [
        "apple", "banana", "orange", 
        "pear", "peach"
        ]
    play_game(word_list)