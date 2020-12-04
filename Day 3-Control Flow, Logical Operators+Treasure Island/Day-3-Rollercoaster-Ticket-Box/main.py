print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
cost = 0
if height >= 120:
  print('You are allowed on the rollercoaster')
  age = int(input("What is your age? "))
  if age < 12:
    print("Your cost is $5")
    cost += 5
  elif age < 18:
    print("Your cost is $7")
    cost += 7
  else:
    if age >= 45 and age <= 55:
      print("Your cost is $0")
      cost += 0
    else: 
      print("Your cost is $12")
      cost += 12
  
  photo = input("Do you want a photo? (y/n) \t")

  if photo == 'y':
    cost += 3
  
  print(f"Your final cost is ${cost}")
  
else:
  print('You are NOT allowed on the rollercoaster')


