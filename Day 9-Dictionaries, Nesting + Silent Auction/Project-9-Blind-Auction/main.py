from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

# deciding the winner -> finding max in dict
def decide_winner():
    max_bid = max(bids.values())
    for bidder in bids:
        if bids[bidder] == max_bid:
            winner = bidder
    print(f"The winner of the auction is {winner} with the bid of ${max_bid} dollars.")

# dict for storing the auction bids
bids = {}

# welcome screen
print(logo)
print("Welcome to the bling auction program")

more_bidders = 'yes'

while more_bidders == 'yes':
    #getting input from the user of the bid
    name = input("Please enter the name for the bid\n")
    bid = int(input("Please enter the price to bid\n"))

    #storing the bid
    bids[name] = bid
    print("Your bid is stored...")

    more_bidders = input('Are there are more bidders? (yes/no)\n')

    if more_bidders == 'yes':
        clear()

# decision for the winner - call our function
decide_winner()

