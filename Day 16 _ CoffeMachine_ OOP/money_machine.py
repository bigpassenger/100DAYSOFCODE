class MoneyMachine:


    def __init__(self):
        self.profit = 0
        self.drinks_price = {
            'latte':2.50,
            'Essperso':1.50,
            'Cappucino':3,
        }
        self.currency ="$"
        self.quarters = {
            'quarters' : 0.25,
            'dimes': 0.10,
            'nickles':0.05, 
            'pennies' : 0.01 
        }


    def report(self):
        """This method prints the profit"""
        print(f'{self.profit}{self.currency} is your profit')
    

    def process_coins(self,cost,drink):
        """This method returns True or False if the coins are equal to the drink's price or not"""
        var = 0
        for value in cost.values():
            var = value + var

        if var == drink.price:
            self.profit = self.profit + var
            return True
        elif var > drink.price:
            change  = drink.price -var
            self.profit = self.profit + var
            print( f'“Here is {self.currency}{round(change,2)} dollars in change.”')
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False
        

    def make_payment(self,drink):
        """This method asks the user for coins and calculates if coins are sufficient. """
        
        print('please insert coins:')
        quarters = int(input('How many quarters'))
        dimes = int(input('How many dimes'))
        nickles = int(input('how many nickles'))
        pennies = int(input('how many pennies'))
        cost = {
            'quarters':quarters*0.25,
            'dimes':dimes*0.10,
            'nickles':nickles*0.05,
            'pennies':pennies*0.01
        }
        result = self.process_coins(cost,drink) 

        if result:
            return True
        else:
            return False