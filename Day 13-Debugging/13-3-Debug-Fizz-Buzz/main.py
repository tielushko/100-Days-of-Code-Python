for number in range(1, 101):
    # must must must use elif here. number 15 would print Fizzbuzz, fizz and buzz altogether
    # also instead of or need and to check for both % 3 AND % 5 (% 15)
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)