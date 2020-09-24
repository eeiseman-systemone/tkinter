from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Learn Tkinter")
root.iconbitmap("icon.ico")

my_img = None

def open():
  global my_img
  root.filename = filedialog.askopenfilename(initialdir="./images", title="Select a File", filetypes=(("jpeg files", "*.jpg"),("all files", "*.*")))
  my_img = ImageTk.PhotoImage(Image.open(root.filename))
  my_label = Label(root, text=root.filename).pack()
  my_image_label = Label(root,image=my_img).pack()

my_button = Button(root, text="open file", command=open).pack()

root.mainloop()
