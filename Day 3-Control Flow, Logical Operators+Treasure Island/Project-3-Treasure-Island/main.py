print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice = input("would you like to go 'left' or 'right'? \n")

if choice.lower() == 'left':
  choice = input("You encountered the big old river right in front of you. You can either try to 'swim' across, or 'wait' for the boatman to pick you up? (swim/wait) \n")
  
  if choice.lower() == 'wait':
    choice = input("You successfully crossed to the other bank, and you see 3 houses with 3 different colored doors. Red, Blue, and Yellow. Which one do you go into? (red/blue/yellow)\n")
    if choice.lower() == 'yellow':
      print("CONGRATULATIONS! YOU FOUND THE TREASURE! YOU WIN!")
    elif choice.lower() == 'red':
      print("You entered the house that is on fire!!! You burned down and you died. :( Game over.")
    elif choice.lower() == 'blue':
      print("You entered the house that is filled with monsters!!! You got eaten and you died. :( Game over.")
    else:
      print('Nah wrong door. A brick fell on your head and you died.')
  else:
    print("You got attacked by an alligator and you got eaten and died :( Game over.")
else:
  print("You fell into a hole in the ground and after breaking your hip you died :( Game over.")
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload