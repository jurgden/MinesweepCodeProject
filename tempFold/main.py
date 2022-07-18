from tkinter import *

# below out "root" and above our "mainloop" is the core internals code of the program
root = Tk()
# Overrides the settings of the window
root.configure(bg="#8CD790")
# window size/resolution
root.geometry('1472x720')
# our top left software window title
root.title("Minesweeper Projx")
# this controls whether or not the user can resize the window (currently false)
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='#AAFCB8',
    width=1472,
    height=180
)

top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='#77AF9C',
    width=368,
    height=540
)

left_frame.place(x=0, y=180)
# Runs the window
root.mainloop()
