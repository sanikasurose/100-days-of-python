# Day 07 - The Hangman Game

## Project Overview

This is a **text-based Hangman game** built in Python as part of my 100 Days of Python challenge.  
The game selects a random word from a list, and the player must guess letters until they reveal the full word or run out of lives.

The project includes:

- Displaying the word with placeholders for unguessed letters
- Tracking previously guessed letters
- Limiting the number of lives
- Showing ASCII art representing the hangman stages
- Informing the player if their guess is correct, incorrect, or already guessed

---

## How to Play

1. Run the `main.py` file.
2. The game will display the initial word as underscores `_`.
3. Guess one letter at a time.
4. The game will update the display with correct guesses and reduce lives for incorrect guesses.
5. The game ends when the player either guesses the full word or runs out of lives.

---

## Skills Learned

During this project, I applied and improved the following Python skills:

- **Randomization**: Using `random.choice()` to select a word from a list
- **Loops**: `for` loops for iterating through word letters, `while` loops for the main game logic
- **Conditionals**: `if`/`elif`/`else` statements to handle correct and incorrect guesses
- **Lists**: Managing guessed letters and placeholders for unguessed letters
- **Strings**: Concatenation, f-strings, and string methods like `.lower()`
- **User Input**: Collecting and validating user input with `input()`
- **Boolean Logic**: Using flags like `game_over` to control the game flow
- **Error Prevention**: Checking for repeated guesses
- **Modules and Imports**: Importing lists, variables, and ASCII art from other Python files

---

## Files Included

- `main.py` — the main game script
- `hangman_words.py` — contains the list of words for the game
- `hangman_art.py` — contains ASCII art for hangman stages and the game logo

---

## Author

Sanika Surose
