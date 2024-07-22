def is_leap(year: int) -> bool:
  divisibleBy4 = year % 4 == 0
  divisibleBy100 = year % 100 == 0
  divisibleBy400 = year % 400 == 0

  return divisibleBy4 and not divisibleBy100 or divisibleBy400

def days_in_month(year: int, month: int) -> int:
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  monthIndex = month - 1
  leap_year = is_leap(year)

  if monthIndex == 1 and leap_year:
    return 29

  return month_days[monthIndex]


year = int(input())
month = int(input())
days = days_in_month(year, month)
print(days)
