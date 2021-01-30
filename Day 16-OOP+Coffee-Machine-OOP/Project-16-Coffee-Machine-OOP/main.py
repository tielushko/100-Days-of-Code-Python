from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
coffee_menu = Menu()
money_machine = MoneyMachine()

operationOver = False

while not operationOver:
    print(coffee_menu.get_items())
    user_command = input("Select the drink from the menu or type 'report' to issue a report ")
    if user_command == 'report':
        print(coffee_machine.report())
        print(money_machine.report())
    elif user_command == 'off':
        operationOver = True
    else:
        menu_item_choice = coffee_menu.find_drink(user_command)
        # if there are enough resources and the user made enough payment we dispense the drink
        if coffee_machine.is_resource_sufficient(menu_item_choice) and money_machine.make_payment(menu_item_choice.cost):
            coffee_machine.make_coffee(menu_item_choice)

