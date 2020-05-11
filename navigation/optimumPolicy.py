"""
this file implements a "realistic" dynamic programming case in which different policies have different costs.
this equates to real world scenarios in which a particular move might be the most direct solution, but for some other reason is undesirable (for instance, a left turn needs to be made, but a car is blocking the left turn lane. in this example the car would do better to avoid the left turn.)
this grid should not be modified, as it was intentionally chosen to best represent this scenario.

"""

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
           
forward_name = ['up', 'left', 'down', 'right']

# right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right

goal = [2, 0]

cost = [2, 1, 20] # right turn, no turn, and a left turn

def optimum_policy2D(grid,init,goal,cost):

    value = [[[999 for col in range(len(grid[0]))] for row in range(len(grid))],
             [[999 for col in range(len(grid[0]))] for row in range(len(grid))],
             [[999 for col in range(len(grid[0]))] for row in range(len(grid))],
             [[999 for col in range(len(grid[0]))] for row in range(len(grid))]]

    policy = [[[' ' for col in range(len(grid[0]))] for row in range(len(grid))],
              [[' ' for col in range(len(grid[0]))] for row in range(len(grid))],
              [[' ' for col in range(len(grid[0]))] for row in range(len(grid))],
              [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]]

    policy2D = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for orientation in range(4):

                    if goal[0] == x and goal[1] == y:
                        if value[orientation][x][y] > 0:
                            value[orientation][x][y] = 0
                            policy[orientation][x][y] = '*'
                            change = True

                    elif grid[x][y] == 0:
                        for i in range(3):
                            o2 = (orientation + action[i]) % 4
                            x2 = x + forward[o2][0]
                            y2 = y + forward[o2][1]

                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                                v2 = value[o2][x2][y2] + cost[i]

                                if v2 < value[orientation][x][y]:
                                    value[orientation][x][y] = v2
                                    policy[orientation][x][y] = action_name[i]
                                    change = True

    x = init[0]
    y = init[1]
    orientation = init[2]

    policy2D[x][y] = policy[orientation][x][y]

    while policy[orientation][x][y] != '*':
        if policy[orientation][x][y] == '#':
            o2 = orientation
        elif policy[orientation][x][y] == 'R':
            o2 = (orientation - 1) % 4
        elif policy[orientation][x][y] == 'L':
            o2 = (orientation + 1) % 4
        x = x + forward[o2][0]
        y = y + forward[o2][1]
        orientation = o2
        policy2D[x][y] = policy[orientation][x][y]

    for i in range(len(policy2D)):
        print(policy2D[i])

    return policy2D

if __name__=="__main__":
    optimum_policy2D(grid,init,goal,cost)
