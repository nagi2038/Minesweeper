from tkinter import Button
import utils
import settings
from dataclasses import dataclass
import random

class Cell:
	all_cells = []
	def __init__(self,x:int, y:int ,is_mine=False) -> None:
		self.is_mine = is_mine
		self.x = x 
		self.y = y 
		self.cell_btn_object = None
		Cell.all_cells.append(self)

	def create_btn_object(self , location:object):
		
		btn = Button(
			location,
			width= settings.GRID_CELL_WIDTH,
			height=settings.GRID_CELL_HEIGHT,
			text = f'{self.x},{self.y}'
			)
		btn.bind('<Button-1>',self.left_click_actions) # left click
		btn.bind('<Button-3>',self.right_click_actions) # right click
		self.cell_btn_object = btn 

	def left_click_actions(self,event):
		# print(event)
		# print("I am left clicked!")
		if self.is_mine:
			self.show_mine()

	def show_mine(self):
		# a logic to interupt the game
		self.cell_btn_object.configure(bg='red')


	def right_click_actions(self,event):
		pass
		# print(event)
		# print("I am right clicked!")


	def __repr__(self):
		return f'{self.__class__.__name__}({self.x}, {self.y})'

	@staticmethod
	def randomize_mines():
		picked_cells = random.sample(
			Cell.all_cells, settings.MINES_COUNT
			 )
		for picked_cell in picked_cells:
			picked_cell.is_mine = True

