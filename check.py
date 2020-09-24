from io import TextIOBase
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Tkinter")
root.iconbitmap("icon.ico")
root.geometry("400x400")

def show():
  mylabel = Label(root, text=var.get()).pack()

# use tkinter variables
var = StringVar()

c = Checkbutton(root, text="Check this Box, I dare you!", variable=var, onvalue="On", offvalue="Off")
# fix initial condition glitch
c.deselect()
c.pack()



mybutton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
