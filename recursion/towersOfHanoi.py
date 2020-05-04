"""
this file implements a recursive solution to the Towers of Hanoi problem, in which a stack of discs must be reorganized from largest to smallest via three poles.
the rules for the problem dictate that a larger disc may never set on top of a smaller disc and that only one disc may be moved at a time.
this problem is essentially unsolvable IRL with a sufficient number of discs (original was 64) due to the astronomical number of required moves.
adapted from Miller & Ranum.

"""
towerA = [4,3,2,1]
towerB = []
towerC = []
def moveTower(stackHeight, fromPole, toPole, viaPole):
    if stackHeight > 0:
        moveTower(stackHeight - 1, fromPole, viaPole, toPole)
        moveDisc(fromPole, toPole)
        moveTower(stackHeight - 1, viaPole, toPole, fromPole)

def moveDisc(fromPole, toPole):
    print("Moving disc from", fromPole, "to", toPole)

def visualMove(stackHeight, fromPole, toPole, viaPole):
    if stackHeight > 0:
        visualMove(stackHeight-1, fromPole, viaPole, toPole)
        toPole.append(fromPole.pop())
        print(towerA, towerB, towerC, '##############', sep="\n")
        visualMove(stackHeight-1, viaPole, toPole, fromPole)

if __name__ == "__main__":
    moveTower(3, "Pole 1", "Pole 2", "Pole 3")
    visualMove(4, towerA, towerB, towerC)
