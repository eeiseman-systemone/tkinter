from tkinter import *

# Always need a root widget
root = Tk()

# define widget into root with text
mylabel01 = Label(root, text="Hello World!")
mylabel02 = Label(root, text="My Name is Eric Eiseman")


# define widget and display at the same time
# mylabel01 = Label(root, text="Hello World!").grid(row=0, column=0)
# mylabel02 = Label(root, text="My Name is Eric Eiseman").grid(row=1, column=5)

# Use grid
# text doesn't move from row/column
# rows/columns are relative, empty rows/columns are ignored
# mylabel01.grid(row=0, column=0)
# mylabel02.grid(row=1, column=5)

# event loop to keep program running
root.mainloop()
