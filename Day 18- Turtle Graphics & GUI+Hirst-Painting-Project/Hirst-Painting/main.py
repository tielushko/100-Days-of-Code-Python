# import colorgram
import turtle
import random

# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors=[]
#
# for color in colors:
# 	r = color.rgb.r
# 	g = color.rgb.g
# 	b = color.rgb.b
# 	color_full = (r, g, b)
# 	rgb_colors.append(color_full)
#
# print(rgb_colors)

color_list = [(201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44),
			  (138, 31, 20), (135, 163, 183), (196,94,75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32),
			  (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176),
			  (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]

t = turtle.Turtle()
s = turtle.Screen()


s.colormode(255)
t.penup()
t.hideturtle()
t.setposition(-300, -300)

for i in range(10):
	for j in range(10):
		color = random.choice(color_list)
		t.dot(20, color)
		t.forward(60)
	t.backward(600)
	t.left(90)
	t.forward(60)
	t.right(90)

s.exitonclick()
