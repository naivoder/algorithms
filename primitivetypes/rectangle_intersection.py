"""
this file implements an algorithm to solve the following problem:
"given two rectangles, with edges parallel to the x and y axis, determine if there exists a non-empty intersection"

the result will return the area of intersection if one exists.
an assumption that the edge qualifies as part of the rectangle is made, meaning two rectangles that share only a perfect corner would still intersect

the method is simply to check the range of x and y values implied by the vertices for potential overlap
this file makes use of namedtuple system instead of Classes

"""
import collections

# x, y correspond to bottom left vertex of rectangle
Rectangle = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))
R1 = Rectangle(x=1, y=2, width=3, height=4)
R2 = Rectangle(x=5, y=3, width=2, height=4)
R3 = Rectangle(x=3, y=3, width=2, height=6)

def intersection(r1:Rectangle, r2:Rectangle) -> Rectangle:
    def is_intersection(r1, r2):
        return (r1.x <= r2.x + r2.width     \
            and r1.x + r1.width >= r2.x     \
            and r1.y <= r2.y + r2.height    \
            and r1.y + r1.height >= r2.y)
    if not is_intersection(r1, r2):
        return Rectangle(0, 0, -1, -1)
    return Rectangle(max(r1.x, r2.x),
                     max(r1.y, r2.y),
                     min(r1.x + r1.width, r2.x + r2.width) - max(r1.x, r2.x),
                     min(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y))

if __name__=="__main__":
    print("###---Rectangle Intersection---###")
    print("R1 and R2:", intersection(R1, R2))
    print("R1 and R3:", intersection(R1, R3))
    print("R2 and R3:", intersection(R2, R3))
