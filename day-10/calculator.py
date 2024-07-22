import os
import art

def add(n1: int, n2: int) -> int:
    return n1 + n2

def subtract(n1: int, n2: int) -> int:
    return n1 - n2

def multiply(n1: int, n2: int) -> int:
    return n1 * n2

def divide(n1: int, n2: int) -> float:
    return n1 / n2

actions = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def pick_action():
  action_string = " ".join(actions.keys())
  action = input(f"Pick an action({action_string}): ")

  if(action not in actions.keys()):
    print("Invalid action. Try again.")
    return pick_action()

  return action

def calculate(n1: int, n2: int, action: str) -> int:
  """Calculate the result of an operation"""
  action = actions[action]
  return action(n1, n2)

def calculator(initial_result = None):
    num1 = int(input("Enter the first number: ")) if initial_result == None else initial_result
    action = pick_action()
    num2 = int(input("Enter the second number: "))

    result = calculate(num1, num2, action)

    print(f"{num1} {action} {num2} = {result}")

    if input("Do you want to continue? (y/n): ") == 'y':
      os.system('clear')
      calculator(result)
    else:
      print("Goodbye!")
      exit(0)

print(art.logo)
calculator()
