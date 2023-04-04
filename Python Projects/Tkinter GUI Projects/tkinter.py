from tkinter import *

root = Tk()

def myClick():  # make something happen so your button does something
  myLable = Label(root, text = "You clicked the button!")
  myLable.pack()

"""
label1 = Label(root, text = "Hello World")
label2 = Label(root, text = "My Name is Jennifer")

# grid is like an array, first location is [0][0], etc
label1.grid(row = 0, column = 0)
label2.grid(row =  1, column = 5)
"""

# padding makes your button bigger
myButton = Button(root, text = "Click Me!", padx = 50, pady = 75, command = myClick) # DON'T do myClick()
# pack() means to put it in the first available spot
myButton.pack()

root.mainloop()
