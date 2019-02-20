import turtle
t = turtle.Pen()
t.speed(100)


            
def circle():
    global siz_e
    for x in range (siz_e):
        t.width(3)
        t.speed(300)
        t.forward(1)
        t.left(1)

def left_spiral():
    global siz_e
    for x in range (siz_e):
        t.forward(x)
        t.left(91)

def right_spiral():
    global siz_e
    for x in range (siz_e):
        t.forward(x)
        t.right(91)

def something():
    global siz_e
    for x in range (siz_e):
        t.forward(x)
        t.right(45)
        t.width(3)

def pen_color():
    colou_r = input("""What color would you like to draw with?
                 Red:1
                 Blue:2
                 Green:3
                 Medium Orchid:4
                 """)
    if colou_r == "1":
        t.pencolor("Red")
    elif colou_r == "2":
        t.pencolor("Blue")
    elif colou_r == "3":
        t.pencolor("Green")
    elif colou_r == "4":
        t.pencolor("Medium Orchid")

def shape_size():
    siz_e = input("How big would you like your shape?")
            
while True:
    pen_color()
    shape_size()
    instruction = input("""What do you want to draw?
                        1: Left spiral
                        2: Right spiral
                        3: Circle
                        4: Something
                        """)
    if instruction == "1":
        left_spiral()
    elif instruction == "2":
        right_spiral()
    elif instruction == "3":
        circle()
    elif instruction == "4":
        something()

