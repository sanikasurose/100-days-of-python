# Day 14 - Higher or Lower: Instagram Followers Game

## Project Overview

This project is a **text-based game** inspired by the "Higher or Lower" concept, built in Python as part of my 100 Days of Python challenge.  
The game compares two Instagram accounts and asks the user to guess **who has more followers**.

The program features:

- Randomly selecting Instagram accounts from a dataset
- Displaying account details (name, description, and country)
- Comparing follower counts and validating the user’s guess
- Score tracking until the user makes a mistake
- Continuous gameplay, with the "loser" account replaced each round

---

## How It Works

1. The game starts by showing two accounts (A and B) with their **name, description, and country**.
2. The user is asked to guess which account has more followers.
3. If the guess is correct:
   - The score increases by 1
   - The game continues, with Account B becoming the new Account A
4. If the guess is incorrect:
   - The game ends
   - The final score is displayed

---

## Skills Demonstrated

- **Python functions** for reusable logic (`format_data`, `check_answer`)
- **Conditional logic** to determine correctness of guesses
- **While loops** for repeatable gameplay
- **Random module** for unpredictable account selection
- **Score tracking** with dynamic updates

---

## Files Included

- **`main.py`** → Contains the game logic
- **`art.py`** → Holds ASCII art for the logo and VS graphic
- **`game_data.py`** → Contains the list of Instagram accounts and their follower counts

---

## Author

Sanika Surose
