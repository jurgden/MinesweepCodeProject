from tkinter import *
from cell import Cell
import settings
import utils


# below out "root" and above our "mainloop" is the core internals code of the program
root = Tk()
# Overrides the settings of the window
root.configure(bg="#8CD790")
# window size/resolution
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
# our top left software window title
root.title("Minesweeper Projx")
# this controls whether or not the user can resize the window (currently false)
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='#AAFCB8',
    width=settings.WIDTH,
    height=utils.height_prct(25)
)

top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='#77AF9C',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)

left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg='#285943',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)

center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell()
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x,
            row=y
        )
# Runs the window
root.mainloop()
