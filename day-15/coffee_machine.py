from data import menu, resources

COINS = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }


def print_report(machine_resources):
    for resource, value in machine_resources.items():
        print(f"{resource.capitalize()}: {value['amount']}{value['unit']}")


def get_command() -> str or None:
    menu_choice = list(menu.keys())
    possible_choice = menu_choice + ["off", "report"]
    choice_string = "/".join(menu_choice)
    user_input = input(f"What would you like? ({choice_string}): ")

    if user_input not in possible_choice:
        print("Invalid choice. Try again.")
        return None

    return user_input


def init_state():
    return {
        "water": {
            "amount": resources["water"],
            "unit": "ml"
        },
        "milk": {
            "amount": resources["milk"],
            "unit": "ml"
        },
        "coffee": {
            "amount": resources["coffee"],
            "unit": "g"
        },
        "money": {
            "amount": 0,
            "unit": "$"
        }
    }


def check_resources(machine_resources, drink):
    for ingredient, amount in menu[drink]["ingredients"].items():
        if machine_resources[ingredient]["amount"] < amount:
            print(f"Sorry there is not enough {ingredient}.")
            return False

    return True


def get_coin():
    total = 0
    for coin, value in COINS.items():
        count = int(input(f"How many {coin}?: "))
        total += count * value

    return total


def transaction(total, drink):
    if total < menu[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False

    change = total - menu[drink]["cost"]
    print(f"Here is ${change} in change.")

    return True


def make_drink(machine_resources, drink):
    for ingredient, amount in menu[drink]["ingredients"].items():
        machine_resources[ingredient]["amount"] -= amount

    machine_resources["money"]["amount"] += menu[drink]["cost"]

    print(f"Here is your {drink}. Enjoy!")

    return machine_resources


def start_machine(machine_resources: dict):
    user_choice = get_command()

    if user_choice is None:
        return True

    if user_choice == "off":
        print("Machine is shutting down.")
        return False

    if user_choice == "report":
        print_report(machine_resources)
        return True

    if not check_resources(machine_resources, user_choice):
        return True

    print("Please insert coins.")
    total = get_coin()
    transaction(total, user_choice)
    make_drink(machine_resources, user_choice)

    return True


def start():
    machine_resources = init_state()
    machine_on = True

    while machine_on:
        machine_on = start_machine(machine_resources)


start()
