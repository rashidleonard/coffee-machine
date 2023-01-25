from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_on = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while turn_on:
    drink = input("What would you like? \n").lower()
    if drink == "off":
        turn_on = False
    elif drink == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if drink in Menu():
            coffee_maker.is_resource_sufficient(drink)








