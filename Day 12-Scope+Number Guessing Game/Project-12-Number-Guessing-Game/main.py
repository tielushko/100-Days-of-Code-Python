import random
from art import logo

EASY_LEVEL_GUESSES = 10 
HARD_LEVEL_GUESSES = 5 

def set_difficulty():
    difficulty_level = input("Choose a difficulty level: (easy/hard) \n")
    # for easy level - assign 10 guesses, for hard - 5 guesses
    if difficulty_level == 'easy':
        return EASY_LEVEL_GUESSES
    elif difficulty_level == 'hard':
        return HARD_LEVEL_GUESSES

def determine_guess(players_guess, target, guess_number):
    if players_guess == target:
        print("You have guessed it correctly! Good job")
        return 0
    elif players_guess > target:
        print("Too high. Guess Again")
        return guess_number - 1
    elif players_guess < target:
        print("Too low. Guess Again")
        return guess_number - 1

def game():
    #TODO 1: print welcome message for the user and ask whether he wants easy or hard level
    print(logo)
    print("I am thinking of the number between 1 and 100.")

    number_of_guesses = set_difficulty()

# pick a random number between 1 and 100 
    number_goal = random.randint(1,100)

    # while we havent run out of guesses    
    while number_of_guesses > 0:
        # make a guess
        print(f"You have {number_of_guesses} remaining to guess a number.")
        user_guess = int(input('Make a guess: '))
        # determine whether the number is too low or too high
        # if the number is on the money, we exit and win

        number_of_guesses = determine_guess(user_guess, number_goal, number_of_guesses)


#start the game
game()