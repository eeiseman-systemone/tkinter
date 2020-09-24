from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Tkinter")
root.iconbitmap("icon.ico")
# Set initial size of the window
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
# be sure to pack it on its own line
vertical.pack()

def slide():
  my_label = Label(root, text=horitonzal.get()).pack()
  root.geometry(str(horitonzal.get()) + "x" + str(vertical.get()))

horitonzal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horitonzal.pack()

# get current value of slider
my_btn = Button(root, text="Click Me!", command=slide).pack()


root.mainloop()
