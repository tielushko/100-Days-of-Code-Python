############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from art import logo
from replit import clear
import random

def pick_card():
    """ Returns a random card from the deck of cards presented to the user"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards_hand):
    """ Function takes a hand of cards, and returns the current score  of the hand.
        In case the score is blackjack with 2 cards and 21 points, it returns 0
        In case of ace in hand and score > 21, it will replace score 11 with 1"""
    
    if len(cards_hand) == 2 and sum(cards_hand) == 21:
        return 0
    
    if 11 in cards_hand and sum(cards_hand) > 21:
        cards_hand[cards_hand.index(11)] = 1

    return sum(cards_hand)

def compare_scores(user_score, dealer_score):
    """ The function takes the score from computer and dealer, then it decides on the winner. """

    if dealer_score > 21 and user_score > 21:
        return "You lose miserably. You went over 21."
    
    if user_score == dealer_score:
        return "It is a draw. Better luck next time."
    elif dealer_score == 0:
        return "You lose. The dealer has a Blackjack :("
    elif user_score == 0:
        return "Congratulations. Blackjack, you win!"
    elif user_score > 21:
        return "Oh man. You went over. You lost."
    elif dealer_score > 21:
        return 'Congrats. You have won!!! Dealer went over 21.'
    elif user_score > dealer_score:
        return 'You win!'
    else: 
        return "You lose!"
    
def setup_hands(computer_hand, user_hand): 
    """initialization of players and computers hands"""
    #imported from repl.it module. For normal operation use import os; os.system('cls') for WIN or os.system('clear') for UNIX
    clear()
    
    # print logo
    print(logo)

    # clear the previous hands of player and dealer
    user_hand.clear()
    computer_hand.clear()

    for i in range(2):
        # adding two cards to the player's deck
        user_hand.append(pick_card())
        # adding two cards to the computer's deck
        computer_hand.append(pick_card())

def play_game():
    """ Setup of the main game functionality for blackjack"""
    isGameOver = False
    
    dealers_hand = []
    players_hand = []
    

    setup_hands(dealers_hand, players_hand)

    while not isGameOver:
        # get the scores from players hands
        players_score = calculate_score(players_hand)
        dealers_score = calculate_score(dealers_hand)

        # display the initial results
        print(f"    Your hand is: {players_hand} and your current score is {players_score}.")
        print(f"    Dealer's first card: {dealers_hand[0]}")

        if players_score == 0 or dealers_score == 0 or players_score > 21:
            isGameOver = True
        else:
            pick_again = input('Would you like to pick another card? Type \'y\' or \'n\' ')
            if pick_again == 'y':
                players_hand.append(pick_card())
            else:
                isGameOver = True

    while dealers_score != 0 and dealers_score < 17:
        dealers_hand.append(pick_card())
        dealers_score = calculate_score(dealers_hand)

    # the results of the final of the game are printed out here

    print(f"     Your final score: {players_score} and your final hand is {players_hand}")
    print(f"     Computer's final score: {dealers_score} and your final hand is {dealers_hand}")
    print(f"{compare_scores(players_score, dealers_score)}")

# the main loop of the game functionality
while input("Would you like to play a game of blackjack (y/n) ") == 'y':
    clear()
    play_game()




##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

