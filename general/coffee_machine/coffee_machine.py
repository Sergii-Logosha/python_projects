# 12.02.23. Sergii Logosha sergiilogosha@gmail.com

# Program simulates a coffee machine. User can get a report of all the
# resources available to machine by typing "report" command, user can choose
# between latte/espresso/cappuccino typing "latte", "espresso", "cappuccino",
# user can stop the program by typing "off", that represents turning the
# machine off

from data_source import MENU, resources


def print_report(source):
    print(f'Water: {source["water"]}ml')
    print(f'Milk: {source["milk"]}ml')
    print(f'Coffee: {source["coffee"]}g')
    print(f'Money: ${money:.2f}')


def check_resources(menu, resources, choice):
    if resources['water'] < menu[choice]['ingredients']['water']:
        print('Sorry there is not enough water.')
        return False
    elif choice in ('latte', 'cappuccino') and \
            resources['milk'] < menu[choice]['ingredients']['milk']:
        print('Sorry there is not enough milk.')
        return False
    elif resources['coffee'] < menu[choice]['ingredients']['coffee']:
        print('Sorry there is not enough coffee.')
        return False
    else:
        return True


def check_money(menu, inserted_money, choice):
    if menu[choice]['cost'] > inserted_money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif menu[choice]['cost'] < inserted_money:
        change = abs(menu[choice]['cost'] - inserted_money)
        print(f"Here is ${change:.2f} dollars in change.")
        return True
    else:
        return True


machine_is_on = True
money = 0.0
while machine_is_on:
    client_choice = input('What would you like? '
                          '(espresso/latte/cappuccino): ').lower()
    if client_choice == 'report':
        print_report(resources)
    elif client_choice in ('espresso', 'latte', 'cappuccino'):
        if not check_resources(MENU, resources, client_choice):
            continue
        print('Please, insert coins.')
        quarters = int(input('How many quarters?: '))
        dimes = int(input('How many dimes?: '))
        nickles = int(input('How many nickles?: '))
        pennies = int(input('How many pennies?: '))
        amount_inserted = (quarters * 0.25) + (dimes * 0.1) + \
                          (nickles * 0.05) + (pennies * 0.01)
        if not check_money(MENU, amount_inserted, client_choice):
            continue
        else:
            money += MENU[client_choice]['cost']
        resources['water'] -= MENU[client_choice]['ingredients']['water']
        resources['coffee'] -= MENU[client_choice]['ingredients']['coffee']
        if client_choice in ("latte", "cappuccino"):
            resources['milk'] -= MENU[client_choice]['ingredients']['milk']
        print(f'Here is your {client_choice}. Enjoy!')
    elif client_choice == 'off':
        machine_is_on = False
