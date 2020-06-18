"""
simulating a board game in which a player must advance through a series of steps to reach the end (eg Candyland)
given an array in which the value of each index represents the maximum number of steps than can be taken from that index

this file implements an algorithm to determine whether a given array contains a valid possiblity of reaching a conclusion
the efficient solution is to keep track of the maximum position reachable from each index (i + a[i])
if at any point an index is reached that is larger than the maximum value stored thus far, the array does not present a valid solution

not a very fun game, per se...

"""
from random import randint

def has_solution(game_board: list) -> bool:
    max_possible, goal_index = 0, len(game_board) - 1
    current_position = 0
    while current_position <= max_possible and max_possible < goal_index:
        max_possible = max(max_possible, current_position + game_board[current_position])
        current_position += 1
    return max_possible >= goal_index

if __name__=="__main__":
    bad_board  = [3, 2, 0, 0, 2, 0, 1]
    good_board = [3, 3, 1, 0, 2, 0, 1]
    rand_board = [randint(0, 3) for int in range(7)]
    print("###---Advance By Offset Game---###")
    print("Bad board has solution?", has_solution(bad_board))
    print("Good board has solution?", has_solution(good_board))
    print("Randomly generated board:", rand_board)
    print("Random board has solution?", has_solution(rand_board))
    
