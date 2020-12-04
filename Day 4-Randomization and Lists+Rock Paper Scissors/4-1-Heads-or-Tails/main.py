#Remember to use the random module 👇

import random;

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

rand_integer = random.randint(0,1)

if rand_integer == 0:
  print("Tails")
elif rand_integer == 1:
  print("Heads")







