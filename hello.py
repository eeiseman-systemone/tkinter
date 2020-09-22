from tkinter import *

# Always need a root widget
root = Tk()

# define widget
mylabel = Label(root, text="Hello World!")

# put widget on screen using pack
# Only make widget as big as its contents
mylabel.pack()

# event loop to keep program running
root.mainloop()
