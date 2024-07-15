print("The Love Calculator is calculating your score...")
name1 = input()
name2 = input()

def check_occurrence(name, word):
  total_occurrence = 0

  for letter in word:
    total_occurrence += name.lower().count(letter.lower())

  return total_occurrence

true_occurrence = check_occurrence(name1, "true") + check_occurrence(name2, "true")
love_occurrence = check_occurrence(name1, "love") + check_occurrence(name2, "love")

love_score = int(str(true_occurrence) + str(love_occurrence))

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
