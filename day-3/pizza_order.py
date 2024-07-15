ALLOWED_SIZE = ["S", "M", "L"]
ALLOWED_BOOL = ["Y", "N"]

SIZE_PRICE_MAP = {
    "S": 15,
    "M": 20,
    "L": 25
}

size = input("What size pizza do you want? S, M, or L: ")

if size not in ALLOWED_SIZE:
    print("Invalid size. Please choose from S, M, or L.")
    exit()

add_pepperoni = input("Do you want pepperoni? Y or N: ")
if add_pepperoni not in ALLOWED_BOOL:
    print("Invalid input. Please choose Y or N.")
    exit()

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese not in ALLOWED_BOOL:
    print("Invalid input. Please choose Y or N.")
    exit()

total = SIZE_PRICE_MAP[size]

if add_pepperoni == "Y":
    if size == "S":
        total += 2
    else:
        total += 3

if extra_cheese == "Y":
    total += 1

print("Thank you for choosing Python Pizza Deliveries!")
print(f"Your final bill is: ${total}.")
