# Day 11 - Blackjack

## Project Overview

This project is a **text-based Blackjack game** implemented in Python as part of my 100 Days of Python challenge.  
It allows the user to play a simplified version of Blackjack against the computer (dealer).

The program features:

- A deck of cards represented as a Python list
- Functions to **deal cards**, **calculate scores**, and **compare results**
- Ace handling: counts as `11` but automatically converts to `1` if the hand goes over 21
- Blackjack detection (score of 21 with the first two cards)
- Dealer logic: the computer (dealer) draws cards until reaching a score of 17 or higher
- User option to "hit" (draw another card) or "pass" (end turn)
- Clear win/lose/tie messages at the end of each round
- ASCII art logo displayed at the start of the game

---

## How to Use

1. Run the `main.py` file.
2. The ASCII art logo will display.
3. You’ll be greeted with:
   - A prompt asking if you’d like to play a game of Blackjack (`y` or `n`).
   - If you choose `y`, both you and the dealer will be dealt two starting cards.
4. Your score and one of the dealer’s cards will be shown.
5. Choose whether to:
   - Type `y` to get another card (hit), or
   - Type `n` to stop drawing cards (pass).
6. The dealer will automatically draw cards until their score is 17 or higher.
7. The program will display both hands and scores, then announce the winner.
8. After each round, you’ll be asked if you’d like to play again.

---

## Skills Learned

During this project, I applied and strengthened the following Python skills:

- **Functions**: Creating reusable functions for dealing cards, calculating scores, comparing results, and controlling the game flow
- **Lists**: Managing the deck of cards and the player/dealer hands
- **Conditionals**: Implementing the rules of Blackjack, including special Ace and Blackjack logic
- **Loops**: Using `while` loops to manage both the game round and continuous replay
- **Random Module**: Selecting random cards from the deck
- **Boolean Logic**: Handling when the game should end (`game_over` flag)
- **User Input**: Interacting with the user to make gameplay decisions
- **Printing & Formatting**: Displaying scores, hands, and game outcomes clearly

---

## Files Included

- `main.py` — the main Blackjack game program
- `art.py` — contains ASCII art for the logo

---

## Author

Sanika Surose
