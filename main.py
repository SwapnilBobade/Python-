from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MoneyMachine = MoneyMachine()
CoffeeMaker = CoffeeMaker()

is_on = True


menu = Menu()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        CoffeeMaker.report()
        MoneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        enough_ingridents = CoffeeMaker.is_resource_sufficient(drink)
        resources_sufficient = MoneyMachine.make_payment(drink.cost)
        if enough_ingridents and resources_sufficient:
            CoffeeMaker.make_coffee(drink)
