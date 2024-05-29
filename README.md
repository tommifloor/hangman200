![The Hangman](/assets/hangman_logo.jpg)

# Hangman

`Hangman` is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the `Hangman` game, where the computer thinks of a word and the user tries to guess it. 

>   ![Static Badge](https://img.shields.io/badge/made%20with-PYTHON-blue) ![Static Badge](https://img.shields.io/badge/made_for-AiCore-red) ![GitHub License](https://img.shields.io/github/license/tommifloor/hangman200)



# Table of Contents
1. [How to Play](#1.-how-to-play)
2. [Requirements](#2.-requirements)
3. [Project Aims](#3.-project-aims)
4. [Project Structure](#4.-project-structure)
5. [License](#5.-license)

## 1. How to Play

`Hangman` is played by running the script via a Python interpreter.

Run the `milestone_4.py` Python script to start the game. Guess letters, receive feedback, and identify the word to win the game.

### Requirements
>No external packages required

## 3. Project Aims

`Hangman` was developed as part of a programming and data engineering course organized by [AiCore](https://www.theaicore.com/). The project aim was develop and demonstrate core competencies in the Python, object-oriented programming, and version control. 

Software and services in development included `VS Code` and `Git`.

## 4. Project Structure

The project is split into 4 `milestone` Python scripts, each  `milestone` script demonstrating progressive stages of the project's development process. 

The `milestone` scripts can be accessed via the `/hangman` folder.

### 1. Milestone 2.py

- Establishes the fundamental components of the `hangman` game: a word list and functions for user input and a random word selector.

### 2. Milestone_3.py

- Adds input validation into the `ask_for_input` function using boolean logic. 
- Adds `check_guess` function to check whether the letter submitted by the user is in the word.

### 3. Milestone_4.py

- Creation of the `Hangman`-class and attributes, including the`num_lives` and `list_of_guesses` attributes to track game progression.
- Adds `check_guess` and `ask_for_input` functions as methods to `Hangman`-class, with additional logic to manage the game cycle.

### 4. Milestone_5.py

- Creates `game` instance of `Hangman`-class.
- Refactores variable and method names for clarity.
- Adds `Docstrings` documentation.

## 5. License
This software is licensed under the [GPL-3.0 license](https://github.com/tommifloor/hangman200/blob/main/COPYING.txt).

---
[Jump to Top](#hangman)
