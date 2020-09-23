from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title("Learn Tkinter")
root.iconbitmap("icon.ico")

# Available message boxes
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
# returns
# Ok,       Ok,          OK,        yes/no,       1/0,        1/0

def popup():
  # catch which button was pressed
  response = messagebox.askyesno("This is my Popup!", "Hello World!")
  Label(root, text=response).pack()
  # if response == 1:
  #   Label(root, text="You Clicked Yes!").pack()
  # else:
  #   Label(root, text="You Clicked No!").pack()

Button(root, text="Popup", command=popup).pack()




root.mainloop()
