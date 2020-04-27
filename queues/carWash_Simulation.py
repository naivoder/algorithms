"""
this file simulates a car wash, comparing outcome of two different "wash qualities" to determine the most advantageous combination of quality/price.
results: lower quality results in potential for highest earnings, but higher quality averages consistently higher earnings per hour
recommendation: business owner should select high quality settings. if visitors did not display tendency to avoid percieved "long" queue lines, the business could strive to maximize income with low quality wash settings.

"""
# problem parameters:
# -------------------
# High quality wash: 5 min, $10.00
# Low quality wash: 2 min, $5.00
# If queue has more than 3 cars, new cars wont join.
# Up to 20 cars per hour => 1/180s avg

import time, random
from queue import Queue

highQuality = (5, 10)
lowQuality = (2, 5)

def carwash(quality):
    washTime = quality[0]
    washCost = quality[1]

    carQueue = Queue()
    washEmpty = True
    clockCount = 1
    earnings = 0; waitTime = 0; carsWashed = 0

    while clockCount <= 3600:

        newCar = random.randint(1, 181)
        if newCar is 180 and carQueue.count() < 4:
            timestamp = clockCount
            carQueue.push(timestamp)

        if washEmpty and not carQueue.isEmpty():
            nextCar = carQueue.pull()
            washEmpty = False
            waitTime = washTime * 60
            earnings += washCost

        else:
            waitTime -= 1

            if waitTime == 0:
                washEmpty = True
                carsWashed += 1

        clockCount += 1

    print("Total earnings this hour:", earnings)
    print("Total number of cars washed:", carsWashed)
    return earnings, carsWashed

if __name__=="__main__":
    print("###---Lower Quality Wash---###")
    for run in range(5):
        carwash(lowQuality)
    print("\n###---Higher Quality Wash---###")
    for run in range(5):
        carwash(highQuality)
