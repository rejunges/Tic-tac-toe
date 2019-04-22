import numpy as np
import copy
import time
from math import inf
from random import choice

class Tictactoe:

	def __init__(self):
		self.grid = [
			[0,0,0],
			[0,0,0],
			[0,0,0]
		]
		self.position = {
			1:[0,0],
			2:[0,1],
			3:[0,2],
			4:[1,0],
			5:[1,1],
			6:[1,2],
			7:[2,0],
			8:[2,1],
			9:[2,2]
		}
		self.computer = "O"
		self.human = "X"
		self.starts = self.human

	def set_computer_human(self, comp, human):
		"""
		Set computer and human symbol.
		Args:
			comp (str): "X" or "O"
			human (str): "X" or "O"
		"""
		self.computer = comp
		self.human = human

	def who_starts(self, player):
		"""
		Set who starts the game
		Args:
			player (str): "X" or "O"
		"""
		self.starts = player

	def state_winner(self, grid, player):
		"""
		Checks if the board/grid has a winning state for the player
		Args:
			grid (list): the state of the current grid
			player (str): "X" or "O"
		Returns:
			bool: True if the grid is a winner state, otherwise, False
		"""

		for i in range(0,3):
			#Verify horizontal
			if (grid[i][0] == player and grid[i][1] == player and grid[i][2] == player):
				return True

			#Verify vertical
			if (grid[0][i] == player and grid[1][i] == player and grid[2][i] == player):
				return True

		#Verify transversal
		if (grid[0][0] == player and grid[1][1] == player and grid[2][2] == player):
			return True

		if (grid[2][0] == player and grid[1][1] == player and grid[0][2] == player):
			return True

		return False

	def free_positions(self, grid):
		"""
		Search for a free position on the board/grid
		Args:
			grid (list): the state of the current grid
		Returns:
			list: list with positions i,j of free position in grid
		"""
		pos = []
		for i in range(0,3):
			for j in range(0,3):
				if grid[i][j] == 0:
					pos.append([i,j])

		return pos
			

	def valid_position(self, pos):
		"""
		Checks if the position is a valid moviment
		Args:
			pos (int): position between 1 to 9
		Returns:
			bool: True if the position is a valid moviment, otherwise False
		"""
		if self.position.get(pos) is None:
			return False

		if self.position.get(pos) in self.free_positions(self.grid):
			return True
		else:
			return False

	def human_turn(self, pos, symbol="X"):
		"""
		Human movement
		Args:
			pos (int): position between 1 to 9
			symbol (str): symbol used by human player
		Returns:
			bool: True if the move is done, otherwise False
		"""
		
		if self.valid_position(pos):
			i, j = self.position.get(pos)
			self.grid[i][j] = symbol
			return True
		return False


	def possible_moves(self, grid, symbol="O"):
		"""
		Based on the grid, inform a list with possible grid for the next iteration  
		Args:
			grid (list): the state of the current grid
			symbol (str): symbol of player
		Returns:
			list: all possible grids
		"""
		grid_list = []
		
		positions = self.free_positions(grid)
		g = grid.copy()	
		for i, j in positions:
			g[i][j] = symbol
			grid_list.append(copy.deepcopy(g))
			g[i][j] = 0
				
		return grid_list

	def computer_turn(self, symbol="O"):
		"""
		Computer movement calculated using the minimax algorithm
		Args:
			symbol (str): symbol used by computer
		"""
		
		depth = len(self.free_positions(self.grid))
		if depth == 9:
			i = choice([0, 1, 2])
			j = choice([0, 1, 2])
			self.grid[i][j] = symbol 
		else:
			best = self.minimax(self.grid, depth, symbol)
			score, grid = best
			self.grid = grid
		
		time.sleep(1)


	def minimax(self, grid, depth, player): 
		""" 
		Minimax algorithm that choose the best movement in grid
		Args:
			grid (list): the state of the grid
			depth (int): how many free position the grid has
			player (str): player ("X" or "O") 
		Returns:
			tuple: score and best move
		"""

		if self.state_winner(grid, "X"):
			return -10 - depth, grid
		if self.state_winner(grid, "O"):
			return 10 + depth, grid
		if depth == 0:
			return 0, grid 

		
		if player == "O":
			best_val = -inf
			best_mov = None
			for move in self.possible_moves(grid, player):
				value, mov = self.minimax(move, depth-1, "X")
				if best_val < value:
					best_val = value
					best_mov = move
			return best_val, best_mov
		
		else:
			best_val = inf
			best_mov = None
			for move in self.possible_moves(grid, player):
				value, mov = self.minimax(move, depth-1, "O")
				if best_val > value:
					best_val = value
					best_mov = move
			return best_val, best_mov
		
	def game_over(self, grid):
		""" 
		Checks if any player wins
		Args:
			grid (list): the state of the current grid
		Returns:
			bool: True if someone wins, otherwise False
		"""
		
		return self.state_winner(grid, "X")  or self.state_winner(grid, "O")