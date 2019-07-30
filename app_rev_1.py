game = [[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]]


def game_board(game_map, player=0, row=0, column=0, just_display=False):
	try:
		print("   A  B  C")
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			print(count + 1, row)

		return game_map
	except IndexError as e:
		print("Error: Make sure you input row/col as 0, 1, or 2", e)
	except Exception as e:
		print("Something went very wrong!", e)


def win(current_game):
	for row in game:
		print(row)
		#### LONG WAY ####
		# all_match = True
		# for item in row:
		# 	if item != row[0]:
		# 		all_match = False
		# if all_match:
		# 	print("WINNER!")
		if row.count(row[0]) == len(row) and row[0] != 0:
			print("WINNER!!")


win(game)


game = game_board(game, just_display=True)
game = game_board(game, player=1, row=2, column=1)