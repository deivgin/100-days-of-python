def prime_checker(num: int, i = None):
  if i == None:
    i = num - 1

  if i == 1:
    print("It's a prime number.")
    return

  if num % i == 0:
    print("It's not a prime number.")
    return

  prime_checker(num, i-1)

n = int(input())
prime_checker(n)
