
def new_canvas():
	"""Create a canvas of 10x10 represented by lists within a list"""
	canvas = []

	for i in range(10):
		canvas.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

	return canvas

def print_canvas(canvas):
	"""Parses the data in the canvas and prints to the terminal"""

	for sublist in canvas:
		output = " "
		for item in sublist:
			output += str(item)

		print(output)

print_canvas(new_canvas())
