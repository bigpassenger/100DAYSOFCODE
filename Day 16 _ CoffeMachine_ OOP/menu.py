class Menue:
    """This class generates the menue and return the user input for the next steps"""
    def __init__(self) -> None:
        self.menue = ['espresso','latte','cappuccino']

    def generate_menue(self):
        print(" “ What would you like? (espresso/latte/cappuccino/):​ ” ")
        self.user_input = str(input())

        if self.user_input in self.menue:
            return self.user_input
        else:
            print("your choice isn't in the menue")