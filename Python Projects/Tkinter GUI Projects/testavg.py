#A previous program prompts a student to enter 3 scores, and then it displays the average. 
#The customer would like the program to have three Entry widgets that the test scores can be entered into, and a button that causes the average to be displayed when clicked.

from tkinter import *

root = Tk()
root.geometry("400x200")

e1 = StringVar()
e2 = StringVar()
e3 = StringVar()

test1 = Label(root, text = "Enter the score for test 1: ").grid(row = 0, column = 0)
test2 = Label(root, text = "Enter the score for test 2: ").grid(row = 1, column = 0)
test3 = Label(root, text = "Enter the score for test 3: ").grid(row = 2, column = 0)

s1 = Label(root, text = " ").grid(row = 3, column = 0)

averageLabel = Label(root, text = "Average:").grid(row = 4, column = 0)

s2 = Label(root, text = " ").grid(row = 5, column = 0)

def average():
  total = float(e1.get()) + float(e2.get()) + float(e3.get())
  avg = total / 3
  calcAvg = Label(root, text = "%s" % avg)
  calcAvg.grid(row = 4, column = 1)

entry1 = Entry(root, textvariable = e1).grid(row = 0, column = 1)
entry2 = Entry(root, textvariable = e2).grid(row = 1, column = 1)
entry3 = Entry(root, textvariable = e3).grid(row = 2, column = 1)
avgButton = Button(root, text = "Average", command = average)
avgButton.grid(row = 6, column = 0)

quitButton = Button(root, text = "Quit", command = root.destroy)
quitButton.grid(row = 6, column = 1)

root.mainloop()
