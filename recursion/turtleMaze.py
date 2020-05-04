"""
this file implements a recursive solution to allow the turtle to escape a generated maze
adapted from M&R
maze.txt file is included in repository, but custom mazes can be made and substituted

"""
import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze:

    def __init__(self, fname):
        rows = 0; columns = 0
        self.grid = []
        maze = open(fname, 'r')
        for line in maze:
            rowlist = []
            col = 0
            for char in line[:-1]:
                rowlist.append(char)
                if char is 'S':
                    self.init = (rows, col)
                col += 1
            rows += 1
            self.grid.append(rowlist)
            columns = len(rowlist)
        self.rows = rows
        self.columns = columns
        self.xmove = - columns / 2
        self.ymove = rows / 2
        self.Timmy = turtle.Turtle(shape='turtle')
        self.window = turtle.Screen()
        self.window.setup(width = 600, height = 600)
        self.window.setworldcoordinates(- (columns - 1) / 2 - .5, - (rows - 1) / 2 - .5, (columns - 1) / 2 + .5, (rows - 1) / 2 + .5)

    def draw(self, debug=False):
        if debug:
            print(self.grid)
        self.Timmy.speed(10)
        for y in range(self.rows):
            for x in range(self.columns):
                if self.grid[y][x] == OBSTACLE:
                    self.box(x + self.xmove, - y + self.ymove, 'tan')
        self.Timmy.color('black', 'blue')

    def box(self, x, y, color):
        self.Timmy.up()
        self.Timmy.goto(x - .5, y - .5)
        self.Timmy.color('black', color)
        self.Timmy.setheading(90)
        self.Timmy.down()
        self.Timmy.begin_fill()
        for i in range(4):
            self.Timmy.forward(1)
            self.Timmy.right(90)
        self.Timmy.end_fill()

    def move(self, x, y):
        self.Timmy.up()
        self.Timmy.setheading(self.Timmy.towards(x + self.xmove, -y + self.ymove))
        self.Timmy.goto(x + self.xmove, -y + self.ymove)

    def dropCrumb(self, color):
        self.Timmy.dot(color)

    def update(self, row, col, val=None):
        if val:
            self.grid[row][col] = val
        self.move(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.dropCrumb(color)

    def exit(self, row, col):
        return (row == 0 or row == self.rows-1 or col == 0 or col == self.columns-1)

    def __getitem__(self, item):
        return self.grid[item]

def escape(maze, start_x, start_y):
    maze.update(start_x, start_y)
    if maze[start_x][start_y] == OBSTACLE:
        return False
    if maze[start_x][start_y] == TRIED or maze[start_x][start_y] == DEAD_END:
        return False
    if maze.exit(start_x, start_y):
        maze.update(start_x, start_y, PART_OF_PATH)
        return True
    maze.update(start_x, start_y, TRIED)
    found = escape(maze, start_x-1, start_y) or \
            escape(maze, start_x+1, start_y) or \
            escape(maze, start_x, start_y-1) or \
            escape(maze, start_x, start_y+1)
    if found:
        maze.update(start_x, start_y, PART_OF_PATH)
    else:
        maze.update(start_x, start_y, DEAD_END)
    return found

if __name__=="__main__":
    maze = Maze('maze.txt')
    maze.draw()
    maze.update(maze.init[0], maze.init[1])
    escape(maze, maze.init[0], maze.init[1])
    maze.window.exitonclick()
