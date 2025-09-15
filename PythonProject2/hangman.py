import random

import hangman_words
import hangman_art

# from hangman_words import word_list
# from hangman_art import stages, logo
lives = 6


logo=hangman_art.logo
print(hangman_art.logo)
stages=hangman_art.stages
print(hangman_art.stages)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder= "_"*len(chosen_word)
print(placeholder)


game_over = False
correct_letters = []

while not game_over:

    print(f"****************************<{lives}>/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"you have already guessed{guess}")
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
        print(f"you guess {guess}, that's not in the word. you lose life")

        if lives == 0:
            game_over =   True

            print(f"***********************IT WAS {chosen_word}YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
