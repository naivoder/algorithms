"""
this file implements a path smoothing algorithm for continuous cyclic motion, using gradient descent to plot optimal points from coordinate list.

"""

from math import *
from copy import deepcopy

path=[[0, 0],
      [1, 0],
      [2, 0],
      [3, 0],
      [4, 0],
      [5, 0],
      [6, 0],
      [6, 1],
      [6, 2],
      [6, 3],
      [5, 3],
      [4, 3],
      [3, 3],
      [2, 3],
      [1, 3],
      [0, 3],
      [0, 2],
      [0, 1]]


def smooth(path, weight_data = 0.1, weight_smooth = 0.1, tolerance = 0.00001):

    newpath = deepcopy(path)
    change = tolerance
    while change >= tolerance:
        change = 0.0
        for i in range(len(path)):
            for j in range(len(path[0])):
                aux = newpath[i][j]
                newpath[i][j] += weight_data * (path[i][j] - newpath[i][j]) + weight_smooth * (newpath[(i-1)%len(path)][j] + newpath[(i+1)%len(path)][j] - 2.0 * newpath[i][j])
                change += abs(aux - newpath[i][j])

    return newpath

if __name__=="__main__":
    newpath = smooth(path)
    for i in range(len(path)):
       print( '['+ ', '.join('%.3f'%x for x in path[i]) +'] -> ['+ ', '.join('%.3f'%x for x in newpath[i]) +']' )
