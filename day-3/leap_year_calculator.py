year = int(input())

divisibleBy4 = year % 4 == 0
divisibleBy100 = year % 100 == 0
divisibleBy400 = year % 400 == 0

leapYear = divisibleBy4 and not divisibleBy100 or divisibleBy400

if leapYear:
  print("Leap year")
else:
  print("Not leap year")
