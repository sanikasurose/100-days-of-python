import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock, Paper and Scissors against the computer.")
user_choice = input("What would you like to play first? Rock, Paper or "
                  "Scissors?\nYour Choice: ")

computer_options = ["Rock", "Paper", "Scissors"]
computer_choice = computer_options[random.randint(0, 2)]

if user_choice == "Rock":
    print(rock)
    if computer_choice == "Rock":
        print(f"Computer's Choice: {computer_choice}")
        print(rock)
        print("Tie.")
    elif computer_choice == "Paper":
        print(f"Computer's Choice: {computer_choice}")
        print(paper)
        print("You lost :(")
    else:
        print(f"Computer's Choice: {computer_choice}")
        print(scissors)
        print("You won!")
elif user_choice == "Paper":
    print(paper)
    if computer_choice == "Rock":
        print(f"Computer's Choice: {computer_choice}")
        print(rock)
        print("You won!")
    elif computer_choice == "Paper":
        print(f"Computer's Choice: {computer_choice}")
        print(paper)
        print("Tie.")
    else:
        print(f"Computer's Choice: {computer_choice}")
        print(scissors)
        print("You lost :(")
elif user_choice == "Scissors":
    print(scissors)
    if computer_choice == "Rock":
        print(f"Computer's Choice: {computer_choice}")
        print(rock)
        print("You lost :(")
    elif computer_choice == "Paper":
        print(f"Computer's Choice: {computer_choice}")
        print(paper)
        print("You won!")
    else:
        print(f"Computer's Choice: {computer_choice}")
        print(scissors)
        print("Tie.")
else:
    print("Not a valid option, try again!")
