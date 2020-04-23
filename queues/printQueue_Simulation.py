"""
this file simulates a print queue, comparing outcome of two different page rates (corresponding to "higher" or "poorer" quality prints) given average use parameters. Modeling this scenario gives insight as to which page rate should be selected. This is my solution to a problem posed by Miller & Ranum. The queue.py abstract class will be used to simultate the FIFO behavior of the print queue.
to modify simulation, for instance doubling the average use, you would increase the "print rate" value. For example if 20 people use the printer in any given hour the high and low print rates respectively would become 12 and 24
the Miller & Ranum solution defines printer and task classes, a better structure and worth looking over for further inspiration...

"""

# problem parameters:
# ------------------
# 1) 10 people using during any given hour
# 2) each person prints up to twice (20/hr; 1/180s avg)     =>      every second, generate random number from 1 to 180 inclusive
# 3) print tasks range from 1 to 20 pages                   =>      generate random number from 1 to 20 (inclusive)
#
# printer configurations:
# ----------------------
# A) 10 pages / minute @ "poorer" quality
#                vs.
# B)  5 pages / minute @ "higher" quality
#
# considerations:
# --------------
# average amount of time task waits in queue?

import time, random
from queue import Queue

highPrintRate = 6 # 10 pages/minute
lowPrintRate = 12 #  5 pages/minute

def printer(printRate):
    # Create a queue of print tasks, each given a timestamp when created
    printQueue = Queue()
    printerFree = True
    waitTimes = []; clockCount = 1; printTime = 0

    # For each second in one hour (3600):
    while clockCount <= 3600:

        # If new print task, add to queue with timestamp
        newTask = random.randint(1, 181)
        if newTask is 180:
            pageLength = random.randint(1, 21)
            timestamp = clockCount
            printQueue.push([timestamp, pageLength])


        # If printer free and task in queue (need flag)
        if printerFree and not printQueue.isEmpty():

            # Remove from queue and assign to printer
            nextTask = printQueue.pull()
            printerFree = False

            # Subtract current time from timestamp to determine wait time
            waitTime = clockCount - nextTask[0]

            # Add wait time to list to calculate average, later
            waitTimes.append(waitTime)

            # Determine print time by number of pages, set variable
            printTime = printRate * nextTask[1]

        # Printer does one second of printing (if necesarry), subtract one second from print time
        else:
            printTime -= 1

            # If print time reaches zero, printer no longer busy
            if printTime == 0:
                printerFree = True

        # Time passes
        clockCount += 1

    # Once complete, compute the average waiting time from wait times generated
    averageWaitTime = sum(waitTimes)/len(waitTimes)
    print("Average wait time at %4.2fs" % averageWaitTime)

    if not printQueue.isEmpty():
        print("%s task(s) remaining in queue..." % printQueue.count())

if __name__=="__main__":
    print("###---Low Print Rate---###")
    for run in range(5):
        printer(lowPrintRate)
    print("\n###---High Print Rate---###")
    for run in range(5):
        printer(highPrintRate)
