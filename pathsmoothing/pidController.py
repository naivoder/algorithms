"""
this file uses the optimal values returned by the twiddle algorithm to implement a PID controller that minimizes drift error 

"""

import random
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from robot import *

def run(robot, tau_p, tau_d, tau_i, n=100, speed=1.0, debug=False):
    myrobot = deepcopy(robot)
    int_crosstrack_error = 0.0
    crosstrack_error = myrobot.y

    x_trajectory = []
    y_trajectory = []

    for i in range(n):
        diff_crosstrack_error = myrobot.y - crosstrack_error
        crosstrack_error = myrobot.y
        int_crosstrack_error += crosstrack_error
        steer = - tau_p * crosstrack_error - tau_d * diff_crosstrack_error - tau_i * int_crosstrack_error
        robot = myrobot.move(steer, speed)
        x_trajectory.append(myrobot.x)
        y_trajectory.append(myrobot.y)
        if debug:
            print(myrobot.x, myrobot.y, myrobot.orientation, steer)

    return x_trajectory, y_trajectory

if __name__=="__main__":
    robot = Robot()
    robot.set(0, 1, 0)

    x_trajectory, y_trajectory = run(robot, 0.2, 3.0, 0.004, debug=True)
    n = len(x_trajectory)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,8))
    ax1.plot(x_trajectory, y_trajectory, 'g', label='PID controller')
    ax1.plot(x_trajectory, np.zeros(n), 'r', label='reference')
