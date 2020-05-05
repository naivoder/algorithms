"""
this file uses the turtle graphics module to create a koch snowflake fractal curve

"""

from turtle import *

def snowflake(length, degree):
    angles = [60, -120, 60, 0]
    if degree > 0:
        for angle in angles:
            snowflake(length/3, degree-1)
            left(angle)
    else:
        forward(length)

if __name__=="__main__":
    color("sky blue", "white")
    bgcolor("black")
    length = 500; degree = 8
    penup()
    backward(length/1.732)
    left(30)
    pendown()
    tracer(100)
    hideturtle()
    begin_fill()
    for i in range(3):
        snowflake(length, degree)
        right(120)
    end_fill()
    update()
    exitonclick()
