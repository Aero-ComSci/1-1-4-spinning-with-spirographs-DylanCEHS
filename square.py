import turtle as trtl
import random

painter = trtl.Turtle()
screen = trtl.Screen()
screen.setup(width=800, height=800)

painter.speed(0)
painter.penup()
painter.goto(-15,15)
painter.pendown()
painter.pensize(4)

x=30

colors = ["red", "orange", "yellow", "blue", "green", "purple"]

while True:
        painter.pencolor(random.choice(colors))
        for j in range(4):
            painter.forward(x)
            painter.right(90)
        if x > 800:
            break 
        painter.penup()
        painter.backward(30)  
        painter.right(90)  
        painter.backward(30) 
        painter.left(90)
        painter.pendown()
        x=x+60





wn = trtl.Screen()
wn.mainloop()
