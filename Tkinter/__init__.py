import tkinter
from tkinter import *
root = Tk()
root.resizable(0,0)
btn = tkinter.Button("button")
counter = 0
if btn.configure().keys():
    counter += 1
print(counter)
root.mainloop()