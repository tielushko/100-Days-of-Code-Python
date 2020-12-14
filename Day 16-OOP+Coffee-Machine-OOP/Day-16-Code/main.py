from turtle import *
from prettytable import PrettyTable

# timmy_turtle = Turtle()
# print(timmy_turtle)
# timmy_turtle.shape('turtle')
# timmy_turtle.color('chartreuse')
# timmy_turtle.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)
