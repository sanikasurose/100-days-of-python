"""
Name: Day 11 - Blackjack
Date: August 19, 2025
Author: Sanika Surose
"""

import random
from art import logo

# Contants
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Functions
def deal_card():
    """Return a random card from the deck."""
    return random.choice(CARDS)

def calculate_score(cards):
    """Calculates the sum of cards; handle Ace as 1 if over 21."""
    score = sum(cards)
    if score == 0 and len(cards) == 2:
        return 0

    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def compare(user_score, comp_score):
    """Compares the user score u_score against the computer score c_score."""
    if user_score == comp_score:
        return "Draw."
    elif comp_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > comp_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    """Game logic function"""
    print(logo)
    user_cards = []
    comp_cards = []
    comp_score = -1
    user_score = -1
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        computer_score = calculate_score(comp_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))


# Game Start
while input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
