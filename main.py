from tkinter import *

root = Tk()
# override the setting of the windows
root.configure(bg="gray") # Setting backgroud color
width, height = (720,480)
root.geometry(f"{width}x{height}") # Width * Height
root.title("Minesweeper Game")
root.resizable(False, False) # to fix Width and Height respectively

top_frame = Frame(
	root,
	bg="red", # color of frame
	width = width,
	height = 80,
)
top_frame.place(x=0,y=0)
left_frame = Frame(
	root,
	bg ="blue",
	width = 120,
	height = root.winfo_screenheight())



left_frame.place(x=0, y=80)
# Run the window
root.mainloop()