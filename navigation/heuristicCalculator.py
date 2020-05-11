"""
this file implements the value calculation required for a-star, returning a heuristic based on current position and known obstacles.
modify the grid to change the navigation space the algorithm must compute.

"""


grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):

    #same size as world, filled with extra large values
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]

    #as long as something is changed, continue updating
    change = True
    while change:

        #must have actually changed something
        change = False

        #check every grid cell in order
        for x in range(len(grid)):
            for y in range(len(grid[0])):

                #check if grid cell is goal
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        change = True

                #for any other unoccupied cell...
                elif grid[x][y] == 0:
                    #try all actions and store result as next step
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        #is this a legitimate state (inside grid and not occupied)
                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:

                            #new value is new cell plus cost of step
                            v2 = value[x2][y2] + cost

                            #if this new value is lower, keep
                            if v2 < value[x][y]:
                                value[x][y] = v2
                                change = True

    for i in range(len(value)):
        print(value[i])

    return value

if __name__=="__main__":
    compute_value(grid,goal,cost)
