# Day 17 - The Quiz Game 📝

## Project Overview

This project is a **True/False quiz game** implemented using **Object-Oriented Programming (OOP)** in Python as part of my 100 Days of Python challenge.  
It allows users to answer a series of computer science questions while keeping track of their score.

The project uses three main classes:

- `Question` → Represents a single quiz question and its correct answer
- `QuizBrain` → Manages the flow of the quiz, asks questions, checks answers, and keeps score
- `question_data` (from `data.py`) → Stores all quiz questions and answers in a structured format

---

## How It Works

1. Questions are loaded from `question_data` into `Question` objects and stored in a list.
2. The `QuizBrain` class iterates through the questions using `next_question()`.
3. The user is prompted to answer each question:

- "Q1: The HTML5 standard was published in 2014. (True/False): "

4. `QuizBrain` checks the user's answer against the correct answer using `check_answer()`.
5. The score is updated, and feedback is printed for each question.
6. After all questions have been asked, the game prints the final score:

- "You've completed the quiz"
- "Your final score was: 7/10"

---

## Skills Demonstrated

- **Object-Oriented Programming**: Classes for questions and quiz logic
- **Encapsulation**: Each class manages its own data and behavior
- **Loops**: Iterates through all quiz questions until completion
- **Conditionals**: Checks answers and provides feedback
- **Lists & Dictionaries**: Stores questions and their associated data
- **User Input**: Collects answers from the user interactively
- **String Formatting**: Displays questions, answers, and scores clearly

---

## Files Included

- `main.py` → Runs the quiz by creating questions and starting the game
- `question_model.py` → Contains the `Question` class
- `quiz_brain.py` → Contains the `QuizBrain` class and quiz logic
- `data.py` → Stores all quiz questions and answers

---

## Author

Sanika Surose
