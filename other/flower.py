"""
a flower for my boss

"""

import turtle

def draw_square(Timmy):
    for index in range(0, 2):
        Timmy.forward(100)
        Timmy.right(30)
        Timmy.forward(100)
        Timmy.right(150)

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")
    Timmy = turtle.Turtle()
    Timmy.sety(50)
    Timmy.shape("turtle")
    Timmy.color("pink")
    Timmy.width(8)
    Timmy.pen(speed=10)

    for index in range(0, 36):
        draw_square(Timmy)
        Timmy.right(10)

    for index in range(0, 4):
        Timmy.circle(50)
        Timmy.right(90)

    Timmy.right(90)
    Timmy.pencolor("green")
    Timmy.fillcolor("green")
    Timmy.forward(300)
    Timmy.right(90)
    Timmy.begin_fill()
    draw_square(Timmy)
    Timmy.left(180)
    draw_square(Timmy)
    Timmy.end_fill()
    Timmy.right(90)
    Timmy.forward(200)
    Timmy.up()
    window.exitonclick()

if __name__=="__main__":
    draw_flower()
