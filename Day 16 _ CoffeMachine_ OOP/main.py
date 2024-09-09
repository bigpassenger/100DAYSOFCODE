from menu import Menu
from coffee_maker import CoffeMaker
from money_machine import MoneyMachine
while True:
    x = Menu()
    x.generate_menue()
    drink = input()
    obj = x.find_drink(drink)
    print(obj.ingredients)
    y = CoffeMaker()
    z = MoneyMachine()
    if y.is_resource_sufficient(obj):
        if z.make_payment(obj):
            y.make_coffee(obj)
            print('Enjoy')
    
    y.report()
    z.report()