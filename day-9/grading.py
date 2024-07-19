student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

def grade(score):
  if score >= 91:
    return "Outstanding"
  elif score >= 81:
    return "Exceeds Expectations"
  elif score >= 71:
    return "Acceptable"
  else:
    return "Fail"

student_grades ={
  key: grade(value) for (key, value) in student_scores.items()
}

print(student_grades)
