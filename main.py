from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
is_on = True
while is_on:
    user_ip = input(f"What would you like ?{menu.get_items()}:")
    if user_ip == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        is_drink_there = menu.find_drink(user_ip)
        is_sufficient = coffee_maker.is_resource_sufficient(is_drink_there)
        if is_sufficient:
            is_money_sufficient = money_machine.make_payment(is_drink_there.cost)
            if is_money_sufficient:
                coffee_maker.make_coffee(is_drink_there)




