import art
import random

RANDOM_NUMBER = random.randint(1, 100)
DIFFICULTIES = ["easy", "hard"]
HARD_ATTEMPTS = 5
EASY_ATTEMPTS = 10

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {RANDOM_NUMBER}")

def get_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

  if difficulty not in DIFFICULTIES:
    print("Invalid input")
    return get_difficulty()

  if difficulty == "easy":
    return EASY_ATTEMPTS
  else:
    return HARD_ATTEMPTS

def guess_number(attempts):
  while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    userInput = input("Make a guess: ")

    if userInput.isnumeric() == False:
      print("Invalid input. Please enter a number.")
      continue

    guess = int(userInput)

    if guess < RANDOM_NUMBER:
      print("Too low.")
    elif guess > RANDOM_NUMBER:
      print("Too high.")
    else:
      print(f"You got it! The answer was {RANDOM_NUMBER}.")
      return

    attempts -= 1

  print("You've run out of guesses, you lose.")

guess_number(get_difficulty())
