from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Tkinter")
root.iconbitmap("icon.ico")

# Image needs to be global to work inside a function with tkinter windows
my_img = ImageTk.PhotoImage(Image.open("images/aspen.png"))

def open():
  global my_img
  top = Toplevel()
  top.title("My Second Window")
  top.iconbitmap("icon.ico")
  my_label = Label(top,image=my_img).pack()
  lbl = Label(top, text="Hellow World!").pack()
  btn2 = Button(top, text="Close Window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()



root.mainloop()
