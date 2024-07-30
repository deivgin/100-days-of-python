class CoffeeMachine:
    """A coffee machine class"""
    def __init__(self, menu):
        self.menu = menu
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints the current resources"""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def check_resources(self, drink):
        """Check if there are enough resources to make the drink"""
        for ingredient, amount in self.menu[drink]["ingredients"].items():
            if self.resources[ingredient] < amount:
                print(f"Sorry there is not enough {ingredient}.")
                return False

        return True

    def make_drink(self, drink):
        """Make the drink"""
        for ingredient, amount in self.menu[drink]["ingredients"].items():
            self.resources[ingredient] -= amount

        print(f"Here is your {drink}. Enjoy!")

    def get_command(self):
        """Get user input as command"""
        menu_choice = list(self.menu.keys())
        possible_choice = menu_choice + ["off", "report"]
        choice_string = "/".join(menu_choice)
        user_input = input(f"What would you like? ({choice_string}): ")

        if user_input not in possible_choice:
            print("Invalid choice. Try again.")
            return None

        return user_input

