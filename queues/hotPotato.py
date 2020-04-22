"""
this file simulates the Josephus problem, aka a game of "hot potato". Rather than encode a number of "passes" to determine the loser of each round, a real game is emulated by starting a timer and allowing the computer to complete as many "passes" as possible during each round. The person left holding the potato when the timer goes off is eliminated from the game!

"""

import time
from queue import Queue

people = ['Bob', 'Linda', 'Gene', 'Luise', 'Tina', 'Teddy', 'Mort']
players = Queue(); roundTime = 10

for person in people:
    players.push(person)

def potato():
    passer = players.pull()
    players.push(passer)
    return players.peek()

def clock(roundTime=None):
    if roundTime is None:
        roundTime = input("How many seconds should each round last? ")
    print("\nIn the game:", players.show())
    print("Starting the clock!")
    timesUp = False
    start = time.time()
    count = 1
    while not timesUp:
        holding = potato()
        end = time.time() - start
        count += 1
        if end >= roundTime:
            timesUp = True
    out = players.pull()
    print("Hot potato was passed %s times..." % count)
    print("%s is out!" % out)
    if players.count() == 1:
        print("%s is the winner!" % players.peek())
    else:
        nextRound = input("Play another round? (y/n) ")
        if nextRound is 'y':
            clock(roundTime)

if __name__=="__main__":
    clock(roundTime)
