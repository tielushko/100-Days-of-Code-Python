#For Loop with Lists
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")

#For Loop with Range

#not including 100, so 1 - 99
for number in range(1, 100):
  print(number)

#1-100
for number in range(1, 101):
  print(number)

#1-10 with step 3: 1 -> 4 -> 7 -> 10
for number in range(1, 11, 3):
  print(number)

#Calculating the sum of all the numbers from 1 to 100.
total = 0
for number in range(1, 101):
  total += number
print(total)