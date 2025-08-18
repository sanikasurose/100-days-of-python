import random
from hangman_words import word_list as word_list
from hangman_art import stages as stages
from hangman_art import logo

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:

    print(logo)
    print(f"****************************{lives}/6 LIVES "
          f"LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try a different letter.")
        continue
    else:
        guessed_letters.append(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)


    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE :( The chosen word was:"
                  f" {chosen_word} **********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
