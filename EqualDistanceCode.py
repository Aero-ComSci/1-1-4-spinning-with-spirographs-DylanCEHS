import turtle as trtl

square_amount = int(input("How many squares do you want? Enter an integer 1-5: "))


painter = trtl.Turtle()
painter.speed(6)
screen = trtl.Screen()
screen.setup(width=800, height=800)
painter.penup()
painter.goto(-300,0)
painter.pendown()

def number_of_squares(square_amount):
    for i in range(square_amount):
        for i in range(4):
            painter.forward(100)
            painter.right(90)
        painter.penup()
        painter.forward(120)
        painter.pendown()

number_of_squares(square_amount)

wn = trtl.Screen()
wn.mainloop()
