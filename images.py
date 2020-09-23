from tkinter import *
# Need pillow
# pip install pillow
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Tkinter")
# Upper left corner icon
root.iconbitmap("icon.ico")

# define the image
my_img = ImageTk.PhotoImage(Image.open("images/aspen.png"))

# put the image in a widget
my_label = Label(image=my_img)

# put widget on screen
my_label.pack()


# Exit button
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


root.mainloop()
