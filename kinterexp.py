import tkinter as tk

import turtle

def right_spiral():
    pen_color()
    shape_size()
    global siz_e
    for x in range (siz_e):
        t.width(1)
        t.forward(x)
        t.right(91)
def left_spiral():
    pen_color()
    shape_size()
    global siz_e
    for x in range (siz_e):
        t.width(1)
        t.forward(x)
        t.left(91)
def something():
    pen_color()
    shape_size()
    global siz_e
    for x in range (siz_e):
        t.width(1)
        t.forward(x)
        t.right(91)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button_1 = tk.Button(frame,
                     text="Right Spiral",
                     fg="green",
                     cammand=right_spiral)
button_1.pack(side+tk.LEFT)

button_2 = tk.Button(frame,
                     text="Left Spiral",
                     fg="blue",
                     comman=left_spiral)
button_2.pack(side=tk.LEFT)

root.mainloop()
