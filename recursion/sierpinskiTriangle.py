"""
this file implements Sierpinksi's Triangle algorithm, dividing an initial triangle into four smaller triangles by connecting the midpoints of each side.
the method requires a given degree, the number of recursive iterations desired.
adapted from example in Miller & Radnum. this is a great visualization of recursion.

"""
import turtle

# draw triangle
def draw(points, color, turtle):
    # set triangle color
    turtle.fillcolor(color)
    # lift tail (don't draw)
    turtle.up()
    # move to starting position
    turtle.goto(points[0][0], points[0][1])
    # drop tail (start draw)
    turtle.down()
    turtle.begin_fill()
    # draw triangle
    turtle.goto(points[1][0], points[1][1])
    turtle.goto(points[2][0], points[2][1])
    turtle.goto(points[0][0], points[0][1])
    # fill with color
    turtle.end_fill()

# find mid-point
def center(top, bottom):
    return ((top[0] + bottom[0]) / 2, (top[1] + bottom[1]) / 2)

# recursive routine
def sierpinski(points, degree, turtle):
    # color map
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'white']
    # draw first triangle
    draw(points, colors[degree % len(colors)], turtle)
    if degree > 0:
        # draw little triangles
        littleTs = {'A':center(points[0], points[1]), 'B':center(points[0], points[2]), 'C':center(points[1], points[2]), 'D':center(points[2], points[1])}
        sierpinski([points[0], littleTs['A'], littleTs['B']], degree - 1, turtle)
        sierpinski([points[1], littleTs['A'], littleTs['C']], degree - 1, turtle)
        sierpinski([points[2], littleTs['D'], littleTs['B']], degree - 1, turtle)

def main():
    Timmy = turtle.Turtle()
    world = turtle.Screen()
    init = [(-400, -200), (0, 400), (400, -200)]
    sierpinski(init, 8, turtle)
    world.exitonclick()

if __name__=="__main__":
    main()
