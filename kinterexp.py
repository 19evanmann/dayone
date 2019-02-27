import tkinter as tk
import turtle 
t = turtle.Pen()
t.speed(100)

root = tk.Tk()

Frame = tk.Frame(root)
Frame.pack()

top_Frame = tk.Frame(root)
top_Frame.pack()

bottom_Frame = tk.Frame(root)
bottom_Frame.pack(side=tk.BOTTOM)

def left_spiral():
    for x in range (200):
        t.width(1)
        t.forward(x)
        t.left(91)

def right_spiral():
    for x in range (200):
        t.width(1)
        t.forward(x)
        t.right(91)

def something():
    for x in range (200):
        t.width(1)
        t.forward(x)
        t.right(187)

def color_red():
    t.pencolor("Red")

def color_blue():
    t.pencolor("Blue")

def color_Medium():
    t.pencolor("Medium Orchid")
    
def shapefr():
    shapeframe = frame(root)
    shapeframe.pack()

def colorfr():
    colorframe = frame(root)
    colorframe.pack()


#Shape Buttons

button = tk.Button(top_Frame, 
                   text="Left Squares", 
                   command=left_spiral)
button.pack(side=tk.LEFT)

button2 = tk.Button(top_Frame,
                   text="Right Squares",
                   command=right_spiral)
button2.pack(side=tk.LEFT)

button3 = tk.Button(top_Frame,
                    text="Spiral-gon",
                    command=something)
button3.pack(side=tk.LEFT)

button4 = tk.Button(bottom_Frame,
                    text="Quit",
                    command=quit)
button4.pack()

#Color Buttons

red_b = tk.Button(Frame,
                  text="Red",
                  fg="Red",
                  command=color_red)
red_b.pack(side=tk.LEFT)

blue_b = tk.Button(Frame,
                   text="Blue",
                   fg="Blue",
                   command=color_blue)
blue_b.pack(side=tk.LEFT)

medium_b = tk.Button(Frame,
                     text="Medium Orchid",
                     fg="Medium Orchid",
                     command=color_Medium)
medium_b.pack(side=tk.LEFT)


root.mainloop()

