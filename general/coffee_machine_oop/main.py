from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_making_module = CoffeeMaker()
money_processing_module = MoneyMachine()

machine_is_on = True
while machine_is_on:
    order_name = input(f'What would you like? ({menu.get_items()}): ')
    if order_name == 'off':
        break
    elif order_name == 'report':
        coffee_making_module.report()
        money_processing_module.report()
    elif order_name in ('latte', 'espresso', 'cappuccino'):
        clients_choice = menu.find_drink(order_name)
        if coffee_making_module.is_resource_sufficient(clients_choice):
            if money_processing_module.make_payment(clients_choice.cost):
                coffee_making_module.make_coffee(clients_choice)
        else:
            continue
    else:
        continue
