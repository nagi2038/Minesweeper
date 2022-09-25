import settings

def height_prct(percent):
	return (settings.HEIGHT/100)*percent

def width_prct(percent):
	return (settings.WIDTH/100)*percent

def grid_cell_width():
	# settings.GRID_CELL_WIDTH = int(width_prct(50))//settings.GRID_SIZE**2
	# print(settings.GRID_CELL_WIDTH)
	settings.GRID_CELL_WIDTH = 10
def grid_cell_height():
	settings.GRID_CELL_HEIGHT = 3

grid_cell_width()
grid_cell_height()
