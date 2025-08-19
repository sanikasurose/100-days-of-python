# Day 12 - The Number Guessing Project

## Project Overview

This project is a **text-based Number Guessing Game** implemented in Python as part of my 100 Days of Python challenge.  
It allows the user to guess a randomly chosen number between **1 and 100**, with limited attempts depending on the chosen difficulty level.

The program features:

- Randomly generated target number between **1 and 100**
- Two difficulty modes:
  - **Easy**: 10 attempts
  - **Hard**: 5 attempts
- A function to check each guess and give feedback ("Too high" / "Too low")
- Decreasing number of attempts with each wrong guess
- Automatic game-over conditions when attempts run out or the correct number is guessed
- ASCII art logo displayed at the start of the program

---

## How to Use

1. Run the `main.py` file.
2. The ASCII art logo will display.
3. You’ll be greeted with:
   - A welcome message explaining the rules.
   - A prompt asking you to choose a difficulty (`easy` or `hard`).
4. A random number between **1 and 100** is generated.
5. Start guessing! After each guess, you will be told whether your guess is **too high** or **too low**.
6. You have a limited number of attempts:
   - 10 attempts on **easy**
   - 5 attempts on **hard**
7. The game ends when:
   - You guess the correct number (win 🎉), or
   - You run out of attempts (lose 😭).

---

## Skills Learned

During this project, I applied and strengthened the following Python skills:

- **Functions**: Breaking the program into reusable functions for checking answers, setting difficulty, and running the game logic
- **Conditionals**: Handling different cases for correct guesses, too high, too low, and running out of turns
- **Loops**: Using a `while` loop to repeatedly prompt the user until the game ends
- **Random Module**: Generating a random number between 1 and 100 using `randint()`
- **Constants**: Defining and using constants for easy/hard difficulty levels
- **User Input**: Collecting guesses and difficulty settings from the user
- **Printing & Formatting**: Giving clear instructions, hints, and feedback to guide the user

---

## Files Included

- `main.py` — the main Number Guessing Game program
- `art.py` — contains ASCII art for the logo

---

## Author

Sanika Surose
