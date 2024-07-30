class MoneyMachine:
    def __init__(self, menu):
        self.menu = menu
        self.money = 0
        self.coins = {
            "quarters": 0.25,
            "dimes": 0.10,
            "nickles": 0.05,
            "pennies": 0.01
        }

    def report(self):
        print(f"Money: ${self.money}")

    def get_coin(self):
        total = 0
        for coin, value in self.coins.items():
            count = int(input(f"How many {coin}?: "))
            total += count * value

        return round(total, 1)

    def process_transaction(self, item):
        total = self.get_coin()

        if total < self.menu[item]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            return False

        self.money += self.menu[item]["cost"]
        change = total - self.menu[item]["cost"]
        print(f"Here is ${change} in change.") if change > 0 else None
        return True
