game = [[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]]


def display_board():
	print("   A  B  C")
	for count, row in enumerate(game):
		print(count + 1, row)


display_board()

game[0][1] = 1

display_board()