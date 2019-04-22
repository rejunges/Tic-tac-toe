import pygame
from pygame.locals import *
from tictactoe import Tictactoe

gainsboro = (220, 220, 220)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 51, 0)
blue = (0, 0, 255)
navy = (0, 0, 128)

def first_screen(background):
	""" 
	Screen of: 'Which symbol do you want to use?'
	Args:
		background (<class 'pygame.Surface'>): surface of pygame
	"""
	background.fill(gainsboro)
	font = pygame.font.Font(None, 40)
	text = font.render("Qual símbolo quer utilizar?", 1, black)
	background.blit(text, (80,250))

	#buttons
	pygame.draw.rect(background, blue,(100,320,150,50))
	pygame.draw.rect(background, navy,(300,320,150,50))
	font = pygame.font.Font(None, 30)
	#text = font.render("X", 1, white)
	#background.blit(text, (170, 335))
	#text = font.render("O", 1, white)
	#background.blit(text, (370, 335))
	text = font.render("Jon Snow", 1, white)
	background.blit(text, (130, 335))
	text = font.render("White Walker", 1, white)
	background.blit(text, (310, 335))
		
def second_screen(background):
	""" 
	Screen of: 'Who should start playing?'
	Args:
		background (<class 'pygame.Surface'>): surface of pygame
	"""
	background.fill(gainsboro)
	font = pygame.font.Font(None, 40)
	text = font.render("Quem deve começar jogando?", 1, black)
	background.blit(text, (80,250))
	
	#buttons
	pygame.draw.rect(background, blue,(100,320,150,50))
	pygame.draw.rect(background, navy,(300,320,150,50))
	font = pygame.font.Font(None, 30)
	text = font.render("Você", 1, white)
	background.blit(text, (150, 335))
	text = font.render("Computador", 1, white)
	background.blit(text, (315, 335))

	
def game_screen(background):
	""" 
	Game screen/grid screen. Board is drawn
	Args:
		background (<class 'pygame.Surface'>): surface of pygame
	"""
	background.fill(gainsboro)
	font = pygame.font.Font(None, 50)
	text = font.render("TIC-TAC-TOE", 1, navy)
	background.blit(text, (150,30))

	#init board
	#Vertical lines
	pygame.draw.line(background, navy, (175,100), (175, 550), 2)
	pygame.draw.line(background, navy, (325,100), (325, 550), 2)

	#Horizonal lines
	pygame.draw.line(background, navy, (25,250), (475, 250), 2)
	pygame.draw.line(background, navy, (25,400), (475, 400), 2)

def check_click_grid(background, pos, game):
	""" 
	Checks if the click  in third screen/game/grid is on the buttons, 
	then, if it is and the movement is valid, the human player makes the move
	Args:
		background (<class 'pygame.Surface'>): surface of pygame
		pos (tuple): position x and y of screen
		game (class 'tictactoe.Tictactoe'): tictactoe game
	Returns:
		bool: True if the movement is done, otherwise False	
	"""
	i,j = pos
	position = -1
	#Upper left
	if (i > 25 and i < 175 and j > 100 and j < 250):
		position = 1
	#Left
	elif (i > 25 and i < 175 and j > 250 and j < 400):
		position = 4
	#Down left
	elif (i > 25 and i < 175 and j > 400 and j < 550):
		position = 7
	#Upper center
	elif (i > 175 and i < 325 and j > 100 and j < 250):
		position = 2
	#Center
	elif (i > 175 and i < 325 and j > 250 and j < 400):
		position = 5
	#Down center
	elif (i > 175 and i < 325 and j > 400 and j < 550):
		position = 8
	#Upper right
	elif (i > 325 and i < 475 and j > 100 and j < 250):
		position = 3
	#right
	elif (i > 325 and i < 475 and j > 250 and j < 400):
		position = 6
	#Down right
	elif (i > 325 and i < 475 and j > 400 and j < 550):
		position = 9
	
	return game.human_turn(position, game.human)

def check_click_first_screen(background, pos, game):
	""" 
	Checks if the click  in first screen is on the buttons
	Args:
		background (<class 'pygame.Surface'>): surface of pygame
		pos (tuple): position x and y of screen
		game (class 'tictactoe.Tictactoe'): tictactoe game
	Returns:
		bool: True if it was, otherwise False	
	"""
	i, j = pos
	screen = 0
	if (i >= 100 and i <= 250 and j >= 320 and j <= 370):
		#Human - "X", Computer - "O"
		screen = 1
		game.set_computer_human("O", "X")
		second_screen(background)
	elif (i >= 300 and i <= 450 and j >= 320 and j <= 370):
		#Human - "O", Computer - "X"
		screen = 1
		game.set_computer_human("X", "O")
		second_screen(background)
	
	return screen

def check_click_second_screen(background, pos, game):
	""" 
	Checks if the click  in second screen is on the buttons
	Args:
		background (<class 'pygame.Surface'>): surface of pygame
		pos (tuple): position x and y of screen
		game (class 'tictactoe.Tictactoe'): tictactoe game
	Returns:
		bool: True if it was, otherwise False	
	"""
	i, j = pos
	screen = 1
	if (i >= 100 and i <= 250 and j >= 320 and j <= 370):
		#You starts
		screen = 2
		game.who_starts(game.human)
		game_screen(background)
	elif (i >= 300 and i <= 450 and j >= 320 and j <= 370):
		#computer starts
		screen = 2
		game.who_starts(game.computer)
		game_screen(background)	

	return screen


def drawn_symbols(background, game):
	""" 
	Drawn symbol "X/jon snow" or "O/white walker" on game's grid
	Args:
		background (<class 'pygame.Surface'>): surface of pygame
		game (class 'tictactoe.Tictactoe'): tictactoe game
	"""
	
	game_screen(background)

	def where_is_symbol(symbol):
		position = []
		for i in range(0,3):
			for j in range(0,3):
				if game.grid[i][j] == symbol:
					position.append([i,j])
		return position
	
	def draw(img):
		for p in pos:
			i,j = p	
			if i == 0:
				if j == 0:
					background.blit(img, (35,100))	
				elif j == 1:
					background.blit(img, (185,100))
				elif j == 2:
					background.blit(img, (335,100))
			elif i == 1:
				if j == 0:
					background.blit(img, (35,250))	
				elif j == 1:
					background.blit(img, (185,250))
				elif j == 2:
					background.blit(img, (335,250))
			elif i == 2:
				if j == 0:
					background.blit(img, (35,400))	
				elif j == 1:
					background.blit(img, (185,400))
				elif j == 2:
					background.blit(img, (335,400))

	#Load images of game of thrones		
	jon_snow = pygame.image.load('imgs/jon_snow.png')
	white_walker = pygame.image.load('imgs/white_walker.png')

		
	font = pygame.font.Font(None, 250)
	text = font.render("X", 1, blue)
	pos = where_is_symbol("X")
	if len(pos) != 0:
		draw(jon_snow) 
	text = font.render("O", 1, navy)
	pos = where_is_symbol("O")
	if len(pos) != 0:
		draw(white_walker)

def print_winner(background, symbol, game, draw = False):
	""" 
	Print winner of the game (You lose, you win, draw) and
	restart button
	Args:
		background (<class 'pygame.Surface'>): surface of pygame
		symbol (str): symbol "X" or "O"
		game (class 'tictactoe.Tictactoe'): tictactoe game
		draw (bool): draw true if there is no winner
	"""

	font = pygame.font.Font(None, 40)
	if draw:
		text = font.render("Empate", 1, navy)
		background.blit(text, (200,570))
	elif symbol == game.human:
		text = font.render("Você venceu", 1, green)
	else:
		text = font.render("Você perdeu", 1, red)
		background.blit(text, (162,570))

	#button to restart
	pygame.draw.rect(background, green, (180, 620,140,50))
	font = pygame.font.Font(None, 30)
	text = font.render("Recomeçar", 1, white)
	background.blit(text, (200, 635))

def check_click_restart(pos, game):
	""" 
	Checks if the click was on the restart button
	Args:
		pos (tuple): position x and y of screen
		game (class 'tictactoe.Tictactoe'): tictactoe game
	Returns:
		bool: True if it was, otherwise False
	"""
	i, j = pos

	if (i >= 180 and i <= 320 and j >= 620 and j <= 670):
		return True
	return False

def interface():
	""" 
	Logic of game, call screens 
	"""
	game = Tictactoe()
	pygame.init()
	background = pygame.display.set_mode((512,700))
	pygame.display.set_caption("Tic-tac-toe")
	game_over = False
	screen = 0
	restart = False
	turn = False
	
	#First screen logic
	first_screen(background)
	while screen == 0 and not game_over:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				game_over = True
			if event.type == pygame.MOUSEBUTTONUP:
				position = pygame.mouse.get_pos()
				screen = check_click_first_screen(background, position, game)
		if not game_over:
			pygame.display.update()
	
	#Second screen logic
	while screen == 1 and not game_over:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				game_over = True
			if event.type == pygame.MOUSEBUTTONUP:
				position = pygame.mouse.get_pos()
				screen = check_click_second_screen(background, position, game)
				
		if not game_over:
			pygame.display.update()
	
	#Game screen logic
	while screen == 2 and not game_over:
		if game.starts == game.human or turn == True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					game_over = True
				if event.type == pygame.MOUSEBUTTONUP:
					position = pygame.mouse.get_pos()
					if not restart and check_click_grid(background, position, game):
						drawn_symbols(background, game)
						pygame.display.update()
						if game.state_winner(game.grid, game.human):
							print_winner(background, game.human, game)
							game_over = True
						game.computer_turn(game.computer)
						drawn_symbols(background, game)
						if game.state_winner(game.grid, game.computer):
							print_winner(background, game.computer, game)
							restart = True
						elif len(game.free_positions(game.grid)) == 0:
							print_winner(background, game.computer, game, True)
							restart = True
					if restart and check_click_restart(position, game):
						restart = False
						game.grid = [
							[0,0,0],
							[0,0,0],
							[0,0,0]
						]
						game_screen(background)
						turn = False
						game.starts = game.human if game.starts == game.computer else game.computer

			if not game_over:
				pygame.display.update()
		else:
			game.computer_turn(game.computer)
			drawn_symbols(background, game)
			pygame.display.update()
			turn = True
	


interface() #start game
