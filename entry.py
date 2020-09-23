from tkinter import *

# Always need a root widget
root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()

# Put default text in the box
e.insert(0, "Enter Your Name: ")

def myclick():
    hello = "Hello " + e.get()
    mylabel = Label(root, text=hello)
    mylabel.pack()

# Don't use the parenthesis with 'command=' otherwise it won't work
mybutton = Button(root, text="Enter Your Name", command=myclick)

mybutton.pack()

# event loop to keep program running
root.mainloop()

