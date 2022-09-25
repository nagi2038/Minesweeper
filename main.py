from tkinter import *
from cell import Cell
import settings
import utils



root = Tk()
# override the setting of the windows
root.configure(bg="gray") # Setting backgroud color
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}") # Width * Height
root.title("Minesweeper Game")
root.resizable(False, False) # to fix Width and Height respectively

top_frame = Frame(
	root,
	bg="black", # color of frame
	width = settings.WIDTH,
	height = utils.height_prct(25),
)

left_frame = Frame(
	root,
	bg ="black",
	width = utils.width_prct(25),
	height = utils.height_prct(75)
	)
center_frame = Frame(
	root,
	bg='green',
	width=utils.width_prct(75),
	height=utils.height_prct(75)
	)

top_frame.place(x=0,y=0)
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))
left_frame.place(x=0, y=utils.height_prct(25))


# c1 = Cell() # for multiple button better to use grid instead of place
# c1.create_btn_object(center_frame)
# c1.cell_btn_object.place(x=0,y=0)

for x in range(settings.GRID_SIZE):
	for y in range(settings.GRID_SIZE):
		c = Cell(x,y)
		c.create_btn_object(center_frame)
		c.cell_btn_object.grid(
			column = x,
			row = y)

Cell.randomize_mines()
# Run the window
# print(Cell.all_cells)
root.mainloop()