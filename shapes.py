
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


def clear_canvas(canvas):
	"""Clears 2 dimensional array by looping over each item to return a clear canvas"""

	for each_list in canvas:
		for i in range(len(each_list)):
			each_list[i] = 0
			print(each_list[i])

	return canvas

def create_rectangle():

	pass

canvas = new_canvas()
print_canvas(canvas)
