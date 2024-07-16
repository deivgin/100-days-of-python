student_heights = [180, 124, 165, 173, 189, 169, 146]
sum = 0
count = 0

for n in student_heights:
  sum += n
  count += 1

average = round(sum / count)

print(f"total height = {sum}")
print(f"number of students = {count}")
print(f"average height = {average}")
