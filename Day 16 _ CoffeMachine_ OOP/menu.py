class MenuItem:
    def __init__(self,name,price,ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

class Menu:
    """This class generates the menue and return the user input for the next steps"""
    def __init__(self) -> None:
        self.menu = [
            MenuItem(name='latte',price=2.50,ingredients={
            'water':200,
            'milk':150,
            'coffee':24
        }),
            MenuItem(name='Essperso',price=1.50,ingredients={
            'water':50,
            'milk':0,
            'coffee':18
        }),
            MenuItem(name='Cappucino',price=3,ingredients={
            'water':250,
            'milk':50,
            'coffee':24
        })
        ]

    def generate_menue(self):
        """prints all the names of the available menu items"""
        
        for item in self.menu:
            print(f"{item.name} costs {item.price}")
            

    def find_drink(self,order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""

        for item in self.menu:
            if item.name == order_name:
                return item
            print("Sorry we don't have your order")