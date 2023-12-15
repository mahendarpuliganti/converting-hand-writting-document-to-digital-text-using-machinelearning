from tkinter import *
import tkinter as tk
from imagetotext import *
root = Tk()

# specify size of window.
root.geometry("1920x1080")

# Create text widget and specify size.
T = Text(root, height = 30, width = 150,font =("Times New Roman", 15))

# Create label
l = Label(root, text = "Detected text:")
l.config(font =("Times New Roman", 20))

Fact = j[1]



# Create an Exit button.
b1 = Button(root, text = "End",command = root.destroy) 

l.pack()
T.pack()
b1.pack()

# Insert The Fact.
T.insert(tk.END, Fact)

tk.mainloop()
print('Done')