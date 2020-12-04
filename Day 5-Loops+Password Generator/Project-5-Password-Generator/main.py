#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

resulting_password = ""
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#generating the random letters
for num in range(nr_letters):
  # 2 possible ways -> the random.choice is much cleaner
  resulting_password += random.choice(letters)
  # random_letter_index = random.randint(0, len(letters) - 1)
  # resulting_password += letters[random_letter_index]

#generating random symbols
for num in range(nr_symbols):
  # 2 possible ways -> the random.choice is much cleaner
  resulting_password += random.choice(symbols)
  # random_symbol_index = random.randint(0, len(symbols) - 1)
  # resulting_password += symbols[random_symbol_index]

for num in range(nr_numbers):
  resulting_password += random.choice(numbers)
  # random_number_index = random.randint(0, len(numbers) - 1)
  # resulting_password += numbers[random_number_index]

print(f"Here is your simple password: {resulting_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


#reset the resulting password
resulting_password = ""
password_length = nr_letters + nr_symbols + nr_numbers

#use 2d array to store all the possible symbols, numbers, letters, 
all_characters = [letters, numbers, symbols]
# use array for counts of the numbers needed remaining.
# use the randomvariable to decrement the number
characters_left = [nr_letters, nr_numbers, nr_symbols]

#run the loop for the length of the password creation - OLEG Solutiion
for num in range(password_length):
  isValid = False
  #picks which character it will pick at random - whether it is the letter, number or symbol.
  # we need to identify the correct random int. if the num of char left is 0 it is not a valid pick, if it isn't its valid.
  while not isValid:
      char_type_randomizer = random.randint(0, 2)
      if characters_left[char_type_randomizer] == 0:
        isValid = False
      else:
        isValid = True  
  
  # decrement the array with counter since we used them up
  characters_left[char_type_randomizer] -= 1
  #pick the index from the character array of the randomizer: letter, number or symbol array
  random_char_index = random.randint(0, len(all_characters[char_type_randomizer]) - 1)
  #add the character from our 2D array.
  resulting_password += all_characters[char_type_randomizer][random_char_index]
  #if our random pick picked among the characters    

print(f'Your strong password is: {resulting_password}')

#Another solution -> generate all the characters as you did in the easy solution, but put them in a list instead, then create a string into which you push the random.choice character from the list.

password_chars = []
resulting_password = ""
#populating the array with random characters
for num in range(nr_letters):
  password_chars.append(random.choice(letters)) 
for num in range(nr_symbols):
  password_chars.append(random.choice(symbols))
for num in range(nr_numbers):
  password_chars.append(random.choice(numbers))

# randomly choosing from the list of the characters and adding them to a string the number of time the total password length is
for num in range(password_length):
  #get the random character and add to password
  random_char = random.choice(password_chars)
  resulting_password += random_char

  #can also instead use password_chars.shuffle() and convert it back to a string

  #make sure to remove that char from array so it doesn't get repeated
  password_chars.remove(random_char)

print(f"Another version of hard password: {resulting_password}")