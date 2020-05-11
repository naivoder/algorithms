"""
this file implements basic obstacle avoidance without attention to cost. the function will return every possible path to the goal.

"""

grid = [['*','.','.','.'],
        ['.','#','.','.'],
        ['.','.','.','.'],
        ['.','.','#','.']]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def every_policy(grid,goal,cost):

    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):

                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        policy[x][y] = '*'
                        change = True

                elif grid[x][y] == '.':
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] != '#':
                            v2 = value[x2][y2] + cost

                            if v2 < value[x][y]:
                                value[x][y] = v2
                                policy[x][y] = delta_name[a]
                                change = True
    for i in range(len(value)):
        print(policy[i])
    return policy

if __name__=="__main__":
    every_policy(grid,goal,cost)
