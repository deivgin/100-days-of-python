from coffee_machine import CoffeeMachine
from money_machine import MoneyMachine
from menu import menu


def main():
    coffee_machine = CoffeeMachine(menu)
    money_machine = MoneyMachine(menu)

    while True:
        user_choice = coffee_machine.get_command()

        if user_choice is None:
            continue

        if user_choice == "off":
            print("Machine is shutting down.")
            break

        if user_choice == "report":
            coffee_machine.report()
            money_machine.report()
            continue

        if not coffee_machine.check_resources(user_choice):
            continue

        print("Please insert coins.")
        transaction_passed = money_machine.process_transaction(user_choice)
        if not transaction_passed:
            continue

        coffee_machine.make_drink(user_choice)


main()