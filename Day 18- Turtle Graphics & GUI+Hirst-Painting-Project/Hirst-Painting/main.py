import colorgram


colors = colorgram.extract('image.jpg', 30)

for color in colors:
	print(color.rgb)