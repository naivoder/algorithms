"""
adapted from M&R, this file is a simple demo of the turtle graphics module

"""
import turtle

turn = ['right', 'left']
Timmy = turtle.Turtle()
Timmys_littleWorld = turtle.Screen()

def spiralIn(turtle, distance, direction):
    if distance > 0:
        turtle.forward(distance)
        if direction == 'right':
            turtle.right(90)
        else:
            turtle.left(90)
        spiralIn(turtle, distance - 5, direction)

def spiralOut(turtle, distance, direction, max=150):
    if distance < max:
        turtle.forward(distance)
        if direction == 'right':
            turtle.right(90)
        else:
            turtle.left(90)
        spiralOut(turtle, distance + 5, direction)

if __name__ == "__main__":
    spiralIn(Timmy, 150, turn[1])
    Timmy.forward(500)
    spiralOut(Timmy, 5, turn[0])
    Timmys_littleWorld.exitonclick()
