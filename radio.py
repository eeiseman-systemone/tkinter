from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Tkinter")
root.iconbitmap("icon.ico")

# tkinter variable not python variable
# r = IntVar()
# r.set("2")

toppings = [
  ("Pepperoni", "Pepperoni"),
  ("Cheese", "Cheese"),
  ("Mushroom", "Mushroom"),
  ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in toppings:
  Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

def clicked(value):
  mylabel = Label(root, text=value)
  mylabel.pack()

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 1", variable=r, value=2, command=lambda: clicked(r.get())).pack()

# mylabel = Label(root, text=pizza.get())
# mylabel.pack()

mybutton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
mybutton.pack()

root.mainloop()
