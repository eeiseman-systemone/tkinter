from tkinter import *

# Always need a root widget
root = Tk()

def myclick():
    mylabel = Label(root, text="Look! I clicked the button")
    mylabel.pack()

# Don't use the parenthesis with 'command=' otherwise it won't work
mybutton = Button(root, text="Click Me!", command=myclick, fg="blue", bg="red")

mybutton.pack()

# event loop to keep program running
root.mainloop()

