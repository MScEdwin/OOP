import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("350x600")

answer = Text(top, height=10, width=40)
answer.place(x=0, y=0)

just_calculated = False


def show(x):
    global just_calculated
    try:
        if x == "=":
            expression = answer.get("1.0", "end-1c")
            result = eval(expression)

            answer.delete("1.0", "end")
            answer.insert("1.0", f"{expression}={result}")
            just_calculated = True
        else:
            # After showing a result, start a new calculation
            if just_calculated:
                answer.delete("1.0", "end")
                just_calculated = False
            answer.insert(tk.INSERT, x)
    except:
        answer.delete("1.0", "end")
        just_calculated = False


def backspace():
    global just_calculated
    if just_calculated:
        answer.delete("1.0", "end")
        just_calculated = False
    else:
        answer.delete("end-2c", "end-1c")  # removes the last character


B1= Button(top, text="1", width=10, height=5, command=lambda: show(1))
B1.place(x=0, y=165)

B2= Button(top, text="2", width=10, height=5, command=lambda: show(2))
B2.place(x=80, y=165)

B3= Button(top, text="3", width=10, height=5, command=lambda: show(3))
B3.place(x=160, y=165)

B4= Button(top, text="+", width=10, height=5, command=lambda: show("+"))
B4.place(x=240, y=165)

B5= Button(top, text="4", width=10, height=5, command=lambda: show(4))
B5.place(x=0, y=250)

B6= Button(top, text="5", width=10, height=5, command=lambda: show(5))
B6.place(x=80, y=250)

B7= Button(top, text="6", width=10, height=5, command=lambda: show(6))
B7.place(x=160, y=250)

B8= Button(top, text="-", width=10, height=5, command=lambda: show("-"))
B8.place(x=240, y=250)

B9= Button(top, text="7", width=10, height=5, command=lambda: show(7))
B9.place(x=0, y=335)

B10= Button(top, text="8", width=10, height=5, command=lambda: show(8))
B10.place(x=80, y=335)

B11= Button(top, text="9", width=10, height=5, command=lambda: show(9))
B11.place(x=160, y=335)

B12= Button(top, text="*", width=10, height=5, command=lambda: show("*"))
B12.place(x=240, y=335)

B12= Button(top, text="0", width=20, height=5, command=lambda: show(0))
B12.place(x=0, y=425)

B12= Button(top, text="=", width=10, height=5, command=lambda: show("="))
B12.place(x=240, y=425)

B13= Button(top, text="/", width=10, height=5, command=lambda: show("/"))
B13.place(x=160, y=425)

# New: backspace button in the free space at the bottom
B14= Button(top, text="⌫", width=43, height=3, command=backspace)
B14.place(x=0, y=510)


top.mainloop()
