import random
import graphics
import words

LIVES = 6

def update_display(display: list, word: str, guess: str):
  for index, letter in enumerate(word):
    if(letter == guess):
      display[index] = guess

  return display

def start():
  lives = LIVES
  chosen_word = random.choice(words.word_list)
  display = ["_" for _ in chosen_word]
  letter_to_guess = len(set(chosen_word))

  print(graphics.logo)

  while(lives > 0 and letter_to_guess > 0):
    guess = input("Guess a letter: ").lower()

    if(guess in chosen_word):
      letter_to_guess -= 1
      display = update_display(display, chosen_word, guess)
      print(f"{' '.join(display)}")
    else:
      lives -= 1
      print(graphics.stages[lives])
      print(f"Remaining lives: {lives}")

  if(lives == 0):
    print(graphics.stages[lives])
    print("You lose!")
  else:
    print("You win!")

start()
