import random
import art

PLAYER_CHOICES = ['y', 'n']
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def pick_card():
  return random.choice(CARDS)

def calculate_score(hand: list[int]) -> int:
  if sum(hand) == 21 and len(hand) == 2:
    return 0

  if sum(hand) > 21 and 11 in hand:
    hand[hand.index(11)] = 1

  return sum(hand)

def dealer_play(dealer_hand: list[int]):
  while calculate_score(dealer_hand) < 17:
    dealer_hand.append(pick_card())

  if calculate_score(dealer_hand) > 21:
    print("Dealer went over. You win!")
    exit()

def player_play(player_hand: list[int]):
  player_choice = input("Type 'y' to get another card, type 'n' to pass: ")

  if player_choice not in PLAYER_CHOICES:
    print("Invalid choice. Please try again.")
    player_play(player_hand)

  if player_choice == 'n':
    return

  player_hand.append(pick_card())
  player_score = calculate_score(player_hand)
  print(f"Your cards: {player_hand}, current score: {player_score}")

  if player_score > 21:
    print("You went over. You lose!")
    exit()

  player_play(player_hand)

def blackjack_phase(player_hand: list[int], dealer_hand: list[int]):
  player_score = calculate_score(player_hand)
  dealer_score = calculate_score(dealer_hand)

  if player_score != 0:
    return

  if player_score == dealer_score:
    print("It's a draw!")
    exit()

  print("You win with a blackjack!")
  exit()

def handle_settlement(player_hand: list[int], dealer_hand: list[int]):
  player_score = calculate_score(player_hand)
  dealer_score = calculate_score(dealer_hand)

  print(f"Your final hand: {player_hand}, final score: {player_score}")
  print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")

  if player_score > dealer_score:
    print("You win!")
  elif player_score < dealer_score:
    print("You lose!")
  else:
    print("It's a draw!")

def start():
  player_hand = [pick_card(), pick_card()]
  dealer_hand = [pick_card(), pick_card()]
  initial_player_score = 21 if calculate_score(player_hand) == 0 else calculate_score(player_hand)

  print(art.logo)
  print(f"Your cards: {player_hand}, current score: {initial_player_score}")
  print(f"Dealer's first card: {dealer_hand[0]}")

  blackjack_phase(player_hand, dealer_hand)
  player_play(player_hand)
  dealer_play(dealer_hand)
  handle_settlement(player_hand, dealer_hand)

start()
