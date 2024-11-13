from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    option = menu.get_items()
    Choice = input(f"what would you like?({option}):")
    if Choice == "OFF":
        is_on = False
    elif Choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(Choice)
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)


