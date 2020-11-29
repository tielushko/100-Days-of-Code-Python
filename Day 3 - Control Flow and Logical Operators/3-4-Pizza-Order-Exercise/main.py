# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total_price = 0

if size == 'S':
  total_price += 15
elif size == 'M':
  total_price += 20
elif size == 'L':
  total_price += 25

if add_pepperoni == 'Y':
  if size == 'S':
    total_price += 2
  elif size == 'M' or size == 'L':
    total_price += 3

if extra_cheese == 'Y':
  total_price += 1

if total_price != 0:
  print(f'Your final bill is ${total_price}')
else:
  print("Invalid input, try again.")