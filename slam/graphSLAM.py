"""
this file implements the graph SLAM algorithm, returning estimated robot position as well as landmark locations after a series of moves. all credit for my understanding of SLAM algorithms goes to Sebastian Thrun! Check out his work for Standford and Google's self-driving car teams.

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

    print(' ')
    print('Landmarks: ', r.landmarks)
    print(r)

    return data

def print_result(N, num_landmarks, result):
    print
    print('Estimated Pose(s):')
    for i in range(N):
        print('    ['+ ', '.join('%.3f'%x for x in result.value[2*i]) + ', ' \
            + ', '.join('%.3f'%x for x in result.value[2*i+1]) +']')
    print
    print('Estimated Landmarks:')
    for i in range(num_landmarks):
        print('    ['+ ', '.join('%.3f'%x for x in result.value[2*(N+i)]) + ', ' \
            + ', '.join('%.3f'%x for x in result.value[2*(N+i)+1]) +']')

def slam(data, N, num_landmarks, motion_noise, measurement_noise):

    #set dimension of filter
    dim = 2 * (N + num_landmarks)

    #make constraint matrix and vector
    omega = matrix()
    omega.zero(dim, dim)
    omega.value[0][0] = 1.0
    omega.value[1][1] = 1.0

    xi = matrix()
    xi.zero(dim,1)
    xi.value[0][0] = world_size / 2.0
    xi.value[1][0] = world_size / 2.0

    #process data
    for k in range(len(data)):

        #index of robot pose
        n = k * 2
        measurement = data[k][0]
        motion      = data[k][1]

        #integrate measurements
        for i in range(len(measurement)):

            #index of landmark pose
            m = 2 * (N + measurement[i][0])

            #update contraints based on measurement
            for b in range(2):
                omega.value[n+b][n+b]   +=  1.0 / measurement_noise
                omega.value[m+b][m+b]   +=  1.0 / measurement_noise
                omega.value[n+b][m+b]   += -1.0 / measurement_noise
                omega.value[m+b][n+b]   += -1.0 / measurement_noise

                xi.value[n+b][0]  += -measurement[i][1+b] / measurement_noise
                xi.value[m+b][0]  +=  measurement[i][1+b] / measurement_noise

        #update constraints based on movement
        for b in range(4):
            omega.value[n+b][n+b]   +=  1.0 / motion_noise
        for b in range(2):
            omega.value[n+b][n+b+2] += -1.0 / motion_noise
            omega.value[n+b+2][n+b] += -1.0 / motion_noise

            xi.value[n+b][0]        += -motion[b] / motion_noise
            xi.value[n+b+2][0]      +=  motion[b] / motion_noise

    #compute estimates
    mu = omega.inverse() * xi
    return mu

if __name__=="__main__":
    num_landmarks      = 5        # number of landmarks
    N                  = 20       # time steps
    world_size         = 100.0    # size of world
    measurement_range  = 50.0     # range at which we can sense landmarks
    motion_noise       = 2.0      # noise in robot motion
    measurement_noise  = 2.0      # noise in the measurements
    distance           = 20.0     # distance by which robot (intends to) move each iteratation

    print("###---Graph SLAM---###")
    data = make_data(N, num_landmarks, world_size, measurement_range, motion_noise, measurement_noise, distance)
    result = slam(data, N, num_landmarks, motion_noise, measurement_noise)
    print_result(N, num_landmarks, result)
