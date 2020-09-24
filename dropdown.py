from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Tkinter")
root.iconbitmap("icon.ico")
root.geometry("400x400")


days = [
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday",
  "Sunday"
  ]

# Use tkinter variable
clicked = StringVar()
clicked.set(days[0])

# use *days to unpack list into positional arguments
# use ** to upack a dictionary into keyword arguments
drop = OptionMenu(root, clicked, *days)
drop.pack()

def show():
  mylabel = Label(root, text=clicked.get()).pack()

mybutton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
