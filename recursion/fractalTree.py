"""
adapted from M&R, this file uses the turtle graphics module to draw a fractal tree

"""
import turtle, random

def drawTree(branchSize, turtle):
    if branchSize > 10:
        turtle.color("brown")
    else:
        turtle.color("green")

    if branchSize > 5:
        subtract = random.randint(0,branchSize//2)
        bend = random.randint(15, 45)
        turtle.width(0.1*branchSize)
        turtle.forward(branchSize)
        turtle.right(bend)
        drawTree(branchSize - subtract, turtle)
        turtle.left(2 * bend)
        drawTree(branchSize - subtract, turtle)
        turtle.right(bend)
        turtle.backward(branchSize)

def main():
    Timmy = turtle.Turtle()
    window = turtle.Screen()
    Timmy.left(90)
    Timmy.up()
    Timmy.backward(100)
    Timmy.down()
    drawTree(75, Timmy)
    window.exitonclick()

if __name__ == "__main__":
    main()
