
def create_canvas():
	"""Create a canvas of 10x10 represented by lists within a list"""
	canvas = []

	for i in range(10):
		canvas.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

	return canvas


def print_canvas(canvas):
	"""Parses through two dimensional array, combines each list a string, and prints to the terminal"""

	for sublist in canvas:
		output = " "
		for item in sublist:
			output += str(item)

		print(output)


def clear_canvas(canvas):
	"""Clears two dimensional array by looping over each item to return a clear canvas"""

	for each_list in canvas:
		for i in range(len(each_list)):
			each_list[i] = 0
			print(each_list[i])

	return canvas



def create_rectangle(start_x, start_y, end_x, end_y, fill_char):
	"""Draws a rectangle given coordinates and character on two-dimensional canvas"""

	canvas_for_rectangle = create_canvas()
	
	for x in range(start_x, end_x + 1, 1):
		for y in range(start_y, end_y + 1, 1):
			canvas_for_rectangle[x][y] = fill_char

	return canvas_for_rectangle



def add_shape_to_canvas(shape, canvas):
	"""Given a two-dimensional shape, the function overlays shape onto two-dimensional canvas and returns canvas"""

	#for each coordinate in canvas if rectangle not 0 for same coordinate, change canvas to rectangle character.
	for x in range(len(shape)):	
		for y in range(len(shape[x])):
			if shape[x][y] != 0:
				canvas[x][y] = shape[x][y]

	return canvas


def change_fill(shape, new_fill):
	"""Changes char of shape in two dimensional array and returns shape"""
	for x in range(len(shape)):	
		for y in range(len(shape[x])):
			if shape[x][y] != 0:
				shape[x][y] = new_fill

	return shape


def translate_position(existing_shape, axis, num):	
	""""""

# axis can only be x or y
# ensure num doesn't put shape off the grid
	translated_shape = create_canvas()

	if axis == 'x':
		for x_index in range(len(existing_shape)):
			existing_shape[x_index + num] = existing_shape[x_index]
			existing_shape[x_index] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			# translated_shape[x_index + num] = existing_shape[x_index]

		#for each x where fill is not 0, get fill and apply to index + num at translated

	elif axis == 'y':
		pass

	else:
		print("not a valid axis")

	existing_shape = translated_shape

	return existing_shape

# canvas = create_canvas()
# print_canvas(canvas)


# Rectangles can overlap with one another. The most recently added rectangle should appear on top of other rectangles. For example:
# Do not render items out of bounds



rect = create_rectangle(1, 1, 3, 3, "*")
# print_canvas(rect)
canvas = create_canvas()
# print_canvas(canvas)
add_shape_to_canvas(rect, canvas)
# print_canvas(canvas)
# print_canvas(rect)
change_fill(rect, "@")
print_canvas(rect)
print()
translate_position(rect, 'x', -1)
print_canvas(rect)



# change the fill on it's own. not once it's been added to the canvas??
# handle cases where coordinates are given off the canvas


#can I create a new canvas under the hood when translating