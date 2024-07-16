INPUT_CONSTRAINT = 1000

target = int(input())

if target < 0 or target > INPUT_CONSTRAINT:
  print("Invalid input")
  exit(1)

sum = 0

for n in range(2, target + 1, 2):
  sum += n

print(sum)
