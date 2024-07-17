# Task for day 7

## The hang man game

Task for this day is to create a simple hangman game. User should be able to guess a letter as an input. If he gets it right, the word with the active letter is drawn, if the guess is wrong, an ascii is shown of hang man being hanged.

### Part 1

- Randomly choose a word from the word_list and assign it to a variable called chosen_word.

- Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

- Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

### Part 2

- Create an empty List called display. For each letter in the chosen*word, add a "*" to 'display'. So if the chosen*word was "apple", display should be ["*", "_", "_", "_", "_"] with 5 "\_" representing each letter to guess.

- Loop through each position in the chosen*word; If the letter at that position matches 'guess' then reveal that letter in the display at that position. e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["*", "p", "p", "_", "_"].

- Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "\_". Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

### Part 3

- Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen*word and 'display' has no more blanks ("*"). Then you can tell the user they've won.

### Part 4

- Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.

- If guess is not a letter in the chosen_word.Then reduce 'lives' by 1. If lives goes down to 0 then the game should stop and it should print "You lose."

- print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
