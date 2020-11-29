# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#TRUE #LOVE
coupled_name = name1.lower() + name2.lower()
love_count_tens =0
love_count_ones = 0

love_count_tens += coupled_name.count("t")
love_count_tens += coupled_name.count("r")
love_count_tens += coupled_name.count("u")
love_count_tens += coupled_name.count("e")

love_count_ones += coupled_name.count("l")
love_count_ones += coupled_name.count("o")
love_count_ones += coupled_name.count("v")
love_count_ones += coupled_name.count("e")


combined_digit_str = str(love_count_tens) + str(love_count_ones)

love_score = int(combined_digit_str)

#if if 
if love_score > 90 or love_score < 10:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
