import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("600x500")


B1= Button(top, text="1", width=10, height=5)
B1.place(x=100, y=150)

B2= Button(top, text="2", width=10, height=5)
B2.place(x=200, y=150)

top.mainloop()