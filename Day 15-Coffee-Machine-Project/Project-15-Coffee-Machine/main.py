from data import MENU, resources

# initialize the variable to control the game length, get the ingredients for each beverage
endOfOperation = False
espresso_ingredients = MENU['espresso']['ingredients']
latte_ingredients = MENU['latte']['ingredients']
cappuccino_ingredients = MENU['cappuccino']['ingredients']


def generate_report():
    """ Function that generates the report about the resources left in the machine """
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')


def dispense_beverage(type_of_beverage):
    """ Function that dispenses the beverage type that is given by the user selection and requests payment """
    # if espresso
    if type_of_beverage == 1:
        # check resources espresso and if true -> request payment from the user, otherwise we say the coffee machine
        # ran out of resources.
        if check_resources(espresso_ingredients['water'], espresso_ingredients['milk'], espresso_ingredients['coffee']):
            request_payment(MENU['espresso']['cost'], 'espresso')
        else:
            print('Not Enough Resources to make the desired drink')
    # latte
    elif type_of_beverage == 2:
        # check resources latte and if true -> request payment from the user, otherwise we say the coffee machine ran
        # out of resources.
        if check_resources(latte_ingredients['water'], latte_ingredients['milk'], latte_ingredients['coffee']):
            request_payment(MENU['latte']['cost'], 'latte')
        else:
            print('Not Enough Resources to make the desired drink')
    # cappuccino
    elif type_of_beverage == 3:
        # check resources espresso and if true -> request payment from the user, otherwise we say the coffee machine
        # ran out of resources.
        if check_resources(cappuccino_ingredients['water'], cappuccino_ingredients['milk'],
                           cappuccino_ingredients['coffee']):
            request_payment(MENU['cappuccino']['cost'], 'cappuccino')
        else:
            print('Not Enough Resources to make the desired drink')
    # in case user enters invalid drink
    else:
        print('Invalid beverage selection')


def check_resources(water_required, milk_required, coffee_required):
    """ Function returns true if there are enough resources for the drink recipe, false otherwise """
    return resources['water'] >= water_required and resources['milk'] >= milk_required and resources[
        'coffee'] >= coffee_required


def request_payment(cost_of_beverage, beverage_type):
    """ This function requests coins from the user and if provided sufficient amount, dispenses coffee """

    # collect all the coins and determine monetary value
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    quarters_value = quarters * 0.25
    dimes_value = dimes * 0.1
    nickels_value = nickels * 0.05
    pennies_value = pennies * 0.01
    total_money_given = quarters_value + dimes_value + nickels_value + pennies_value

    # in case the user didn't provide enough money, we refund and return
    if total_money_given < cost_of_beverage:
        print(f"Insufficient balance. Your ${total_money_given} are refunded.")
    # dispense beverage and give change
    else:
        print(f"{beverage_type} is dispensing... Enjoy!")
        change = total_money_given - cost_of_beverage
        print(f"Here's your change of ${change}!")
        # remove resources from the coffee machine
        subtract_resources(cost_of_beverage, beverage_type)


def subtract_resources(cost_of_beverage, beverage_type):
    resources['water'] -= MENU[beverage_type]['ingredients']['water']
    resources['milk'] -= MENU[beverage_type]['ingredients']['milk']
    resources['coffee'] -= MENU[beverage_type]['ingredients']['coffee']
    resources['money'] += cost_of_beverage


while not endOfOperation:
    # TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
    print("Welcome to the coffee machine! Please take a look at our menu!")
    print("\n1. Espresso: $1.5\n2. Latte: $2.5\n3. Cappuccino: $3.0\n")
    command_selection = input(
        'Select the beverage you would like (1./2./3.) or "report" to display the machine\'s resources ')

    if command_selection == 'report':
        generate_report()
    elif command_selection == 'off':
        endOfOperation = True
    else:
        int_command = int(command_selection)
        dispense_beverage(int_command)

# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

# TODO 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.

# TODO 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

# TODO 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “ Sorry there is not enough water. ”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.


# TODO 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# TODO 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “ Sorry that's not enough money. Money refunded. ”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.


# TODO 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
