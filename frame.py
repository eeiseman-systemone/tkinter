from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Tkinter")
root.iconbitmap("icon.ico")

# Padding on the inside of the frame border
frame = LabelFrame(root, text="This a my Frame...", padx=50, pady=50)

b = Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="...Or Here!")
# Can use grid inside frame while packing the whole frame
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

# Padding on the outside of the frame border
frame.pack(padx=10, pady=10)




root.mainloop()
