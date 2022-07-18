from tkinter import *

# below out "root" and above our "mainloop" is the core internals code of the program
root = Tk()
# window size/resolution
root.geometry('1472x720')
# our top left software window title
root.title("Minesweeper Projx")
# this controls whether or not the user can resize the window (currently false)
root.resizable(False, False)
root.mainloop()
