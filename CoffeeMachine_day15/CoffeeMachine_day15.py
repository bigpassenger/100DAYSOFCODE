# TODO importing available ingredients
ingredients = {
    'water': 50,
    'milk': 200,
    'coffee': 100,
    'money': 2.5
}


# TODO define a function to see how many ingredients left
def report(ingredients):
    print(ingredients)
# TODO define a function for processing the user's request


def request_function(request, **ingredients):
    if request == 'Espresso':
        if ingredients['water'] >= 50 and ingredients['coffee'] >= 18:
            ingredients['water'] -= 50
            ingredients['coffee'] -= 18
            return True,ingredients
        else:
            print('Sorry not enough ingredients are currently available')
            return False
    elif request == 'latte':
        if ingredients['water'] >= 200 and ingredients['coffee'] >= 24 and ingredients['milk'] >= 150:
            ingredients['water'] -= 200
            ingredients['coffee'] -= 24
            ingredients['milk'] -= 150
            return True, ingredients
        else:
            print('Sorry not enough ingredients are currently available')
            return False


def exchange(request):
    print('please insert coins')
    quarters = int(input('How many quarters'))
    dimes = int(input('How many dimes'))
    nickles = int(input('how many nickles'))
    pennies = int(input('how many pennies'))
    value = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if request == 'Espresso' and value > 1.50:
        change = value - 1.50
        return True, change
    elif request == 'latte' and value > 2.50:
        change = value - 2.50
        return True, change
    else:
        print('Not Enough coin')
        return False


# TODO define a function to make coffee
def coffeemaker():
    print("here you're enjoy your coffee")


# TODO define a while loop for creating texts and getting inputs from user
while True:
    print("What would you like? (Espresso/latte/cappuccino):")
    UserRequest = str(input())
    if UserRequest == 'off':
        break
    elif UserRequest == 'report':
        report(ingredients)
    elif UserRequest == 'Espresso' or UserRequest == 'latte':
        status,ingredients = request_function(UserRequest, **ingredients)
        status2,coin = exchange(UserRequest)
        if status and status2 is True:
            coffeemaker()
            print('here is ' + str(round(coin, 2)) + '$' + 'for change')
        else:
            continue
