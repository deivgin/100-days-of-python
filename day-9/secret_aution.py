import os
import art

def clear():
    os.system("clear")

def add_bidder(bidders: list):
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))

  bidders.append({
    "name": name,
    "bid": bid
  })

def run(bidders):
  add_bidder(bidders)
  new_bidder = input("Are there any other bidders? Type 'yes' or 'no' ")

  if(new_bidder == "yes"):
    clear()
    run(bidders)

def find_winner(bidders):
  highest_bidder = bidders[0]

  for bidder in bidders:
    if bidder["bid"] > highest_bidder["bid"]:
      highest_bidder = bidder

  return highest_bidder

def start():
  print(art.logo)
  bidders = []

  run(bidders)
  winner = find_winner(bidders)

  print(f"The winner is {winner['name']} with a bid of ${winner['bid']}")

start()
