"""
this file implements the 'online' modification of the graph SLAM algorithm, which stores only the most recent robot positional data while expanding the map location data as more landmarks are discovered

"""

from robot import *
from matrix import *

def make_data(N, num_landmarks, world_size, measurement_range, motion_noise, measurement_noise, distance):
    complete = False

    while not complete:
        data = []
        r = Robot(world_size, measurement_range, motion_noise, measurement_noise)
        r.make_landmarks(num_landmarks)
        seen = [False for row in range(num_landmarks)]

        # initial guess
        orientation = random.random() * 2.0 * pi
        dx = cos(orientation) * distance
        dy = sin(orientation) * distance

        for k in range(N-1):

            # sense
            Z = r.sense()

            # check off all landmarks that were observed
            for i in range(len(Z)):
                seen[Z[i][0]] = True

            # move
            while not r.move(dx, dy):
                # if we'd be leaving the robot world, pick instead a new direction
                orientation = random.random() * 2.0 * pi
                dx = cos(orientation) * distance
                dy = sin(orientation) * distance

            # memorize data
            data.append([Z, [dx, dy]])

        # we are done when all landmarks were observed; otherwise re-run
        complete = (sum(seen) == num_landmarks)

    print('Landmarks: ', r.landmarks)
    print(r)

    return data

def print_result(N, num_landmarks, result):
    print('Estimated Pose(s):')
    for i in range(N):
        print('    ['+ ', '.join('%.3f'%x for x in result.value[2*i]) + ', ' \
            + ', '.join('%.3f'%x for x in result.value[2*i+1]) +']')
    print('Estimated Landmarks:')
    for i in range(num_landmarks):
        print('    ['+ ', '.join('%.3f'%x for x in result.value[2*(N+i)]) + ', ' \
            + ', '.join('%.3f'%x for x in result.value[2*(N+i)+1]) +']')

def online_slam(data, N, num_landmarks, motion_noise, measurement_noise):
    #set dimensions
    dim = 2 * (1 + num_landmarks)

    #define constraint matrices
    omega = matrix()
    omega.zero(dim, dim)
    xi = matrix ()
    xi.zero(dim, 1)

    #set initial position
    omega.value[0][0] = 1.0
    omega.value[1][1] = 1.0

    xi.value[0][0] = world_size / 2.0
    xi.value[1][0] = world_size / 2.0

    #process data
    for k in range(len(data)):
        measurement = data[k][0]
        motion      = data[k][1]

        #integrate measurements
        for i in range(len(measurement)):

            #index of landmark position
            m = 2 * (1 + measurement[i][0])

            #update constraints based on measurement
            for b in range(2):
                omega.value[b][b]       +=  1.0 / measurement_noise
                omega.value[m+b][m+b]   +=  1.0 / measurement_noise
                omega.value[b][m+b]     += -1.0 / measurement_noise
                omega.value[m+b][b]     += -1.0 / measurement_noise

                xi.value[b][0]      += -measurement[i][1+b] / measurement_noise
                xi.value[m+b][0]    +=  measurement[i][1+b] / measurement_noise

        r = range(4, dim+2)
        rng = list(r)
        lst = [0, 1] + rng
        omega = omega.expand(dim+2, dim+2, lst, lst)
        xi = xi.expand(dim+2, 1, lst, [0])

        #update constraint matrix based on movement
        for b in range(4):
            omega.value[b][b]   +=  1.0 / motion_noise
        for b in range(2):
            omega.value[b][b+2] += -1.0 / motion_noise
            omega.value[b+2][b] += -1.0 / motion_noise

            xi.value[b][0]      += -motion[b] / motion_noise
            xi.value[b+2][0]    +=  motion[b] / motion_noise

        #factor out previous pose
        newlist = range(2, len(omega.value))
        a = omega.take([0,1], newlist)
        b = omega.take([0,1])
        c = xi.take([0,1], [0])
        omega = omega.take(newlist) - a.transpose() * b.inverse() * a
        xi = xi.take(newlist, [0]) - a.transpose() * b.inverse() * c

    #compute best estimate
    mu = omega.inverse() * xi
    return mu, omega

if __name__=="__main__":
    num_landmarks      = 5        # number of landmarks
    N                  = 20       # time steps
    world_size         = 100.0    # size of world
    measurement_range  = 50.0     # range at which we can sense landmarks
    motion_noise       = 2.0      # noise in robot motion
    measurement_noise  = 2.0      # noise in the measurements
    distance           = 20.0     # distance by which robot (intends to) move each iteratation

    print("###---Online SLAM---###")
    data = make_data(N, num_landmarks, world_size, measurement_range, motion_noise, measurement_noise, distance)
    result = online_slam(data, N, num_landmarks, motion_noise, measurement_noise)
    print_result(1, num_landmarks, result[0])
