"""
this file implements the twiddle algorithm, for determining optimal parameters. the test case demonstrates the selection of proportional, integral and derivative controller values for a self-driving car attempting to minimize drift error.

"""

import random
import numpy as np
import matplotlib.pyplot as plt
from robot import *

def make_robot():
    robot = Robot()
    robot.set(0.0, 1.0, 0.0)
    robot.set_steering_drift(10.0 / 180.0 * np.pi)
    return robot

# PID controller used to minimize crosstrack error
def run(robot, params, n=100, speed=1.0):
    x_trajectory = []
    y_trajectory = []
    err = 0
    prev_cte = robot.y
    int_cte = 0
    for i in range(2 * n):
        cte = robot.y
        diff_cte = cte - prev_cte
        int_cte += cte
        prev_cte = cte
        steer = -params[0] * cte - params[1] * diff_cte - params[2] * int_cte
        robot.move(steer, speed)
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)
        if i >= n:
            err += cte ** 2
    return x_trajectory, y_trajectory, err / n

# twiddle algorithm to determine optimal values
def twiddle(tol=0.2):
    p = [0.0, 0.0, 0.0]
    dp = [1.0, 1.0, 1.0]
    robot = make_robot()
    x_trajectory, y_trajectory, best_err = run(robot, p)
    while sum(dp) > tol:
        for i in range(len(p)):
            p[i] += dp[i]
            robot = make_robot()
            err = run(robot, p)[2]
            if err < best_err:
                best_err = err
                dp[i] *= 1.1
            else:
                p[i] -= 2.0* dp[i]
                robot = make_robot()
                err = run(robot, p)[2]
                if err < best_err:
                    best_err = err
                    dp[i] *= 1.1
                else:
                    p[i] += dp[i]
                    dp[i] *= 0.9

    return p, best_err

if __name__ == "__main__":
    params, err = twiddle()
    print("Optimal parameters =", params)
    print("Final twiddle error = {}".format(err))

    robot = make_robot()
    x_trajectory, y_trajectory, err = run(robot, params)
    n = len(x_trajectory)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
    ax1.plot(x_trajectory, y_trajectory, 'g', label='Twiddle PID controller')
    ax1.plot(x_trajectory, np.zeros(n), 'r', label='reference')
