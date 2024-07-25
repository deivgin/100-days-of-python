import art
import data
import random
import os

PLAYER_INPUTS = ["a", "b"]

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def get_random_game_data(game_data_set: list):
  random_index = random.randint(0, len(game_data_set) - 1)
  return game_data_set.pop(random_index)

def get_player_input():
  answer = input("Who has more followers? Type 'a' or 'b': ")

  if answer not in PLAYER_INPUTS:
    print(f"Invalid input. Correct inputs are {PLAYER_INPUTS}")
    return False

  return answer

def game(account_a, account_b):
  print(f"Compare {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
  print(art.vs)
  print(f"Against {account_b['name']}, a {account_b['description']}, from {account_b['country']}")

  answer = get_player_input()

  while not answer:
    answer = get_player_input()

  if answer == "a":
    return account_a['follower_count'] > account_b['follower_count']
  else:
    return account_b['follower_count'] > account_a['follower_count']

def start():
  game_data = data.data
  game_over = False
  score = 0

  account_a = get_random_game_data(game_data)
  account_b = get_random_game_data(game_data)

  while not game_over:
    clear()
    print(art.logo)

    if len(game_data) < 2:
      print(f"Congratulations! You have completed the game with a score of {score}")
      game_over = True
      break

    round_result = game(account_a, account_b)

    if round_result:
      score += 1
      account_a = account_b
      account_b = get_random_game_data(game_data)
      print(f"Correct! Current score: {score}")
    else:
      game_over = True
      print(f"Sorry, that's wrong. Final score: {score}")



start()
