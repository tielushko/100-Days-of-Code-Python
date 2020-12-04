#choose a random word
import random
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)

# variable for keeping track of user lives
lives = 6

# print name of game
print(logo)

# Creating Blanks
display = []
for letter in chosen_word:
    display.append('_')

# while there are blanks in the in word
while '_' in display:

    # prompting user for the guess
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"Hmmm, I think you already guessed the letter '{guess}' ...")

    # revealing the letter if it was guessed correctly
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = guess
    # printing the user's guess on the screen

    # if the guessed letter is not in the word, we reduce lives and update hangman 
    if not guess in chosen_word:
        print("Ooops o_O that letter is not in the word, you lose a life :(")
        lives -= 1
        print(stages[lives])
    
    # once the lives is 0 we lose and exit
    if lives == 0:
        print(f'You lose, the correct word was {chosen_word}')
        break

    # print at each correct stage, join the elements into a string separated by spaces
    print(f"{' '.join(display)}")

# if we have some lives left and we got rid of all the _ we win!
if lives != 0:
    print('You win!')