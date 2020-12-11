############DEBUGGING#####################

# # Describe Problem
# The problem is that the function never reaches i = 20 to print the statement you got it
# In this function, the i in the for loop is running between the range 1 - 20 NON-INCLUSIVE since range function is noninclusively bound. 
# def my_function():
#   for i in range(1, 20): '
# bug fix: 
# for i in range(1,21):
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
# The bug happens when rand int becomes 6 and it throws IndexError
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = 6
# #dice_num = randint(1, 6) 
# #to fix the error -> 
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# Play Computer
# Select 1994. Evaluate each line of code to see which statement will execute - none of these statements will execute
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# # indent the block after if
# # since the string age was not parsed to integer we get ValueError
# # then the age variable does not show up in print because we aren't using an f string.
# # fix -> int()
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# print(pages)
# # instead of assignment with = the program compares with ==
# # word_per_page == int(input("Number of words per page: "))
# word_per_page = int(input("Number of words per page: "))
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    # the b_list.append was not indented in the for loop -> it was inserting the very last new_item: indent
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

# Tip 7: Take a break

# Tip 8: Run code often

# Tip 9: Ask a friend

# Tip 10: Ask StackOverflow